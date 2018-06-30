#!/usr/bin/env python
"""
This script reads checkerboard calibration images and pickles the calculated calibration params.
"""

import glob
import pickle
import numpy as np

import cv2

CAL_COL_CNT = 9
CAL_ROW_CNT = 6

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((CAL_ROW_CNT*CAL_COL_CNT,3), np.float32)
objp[:,:2] = np.mgrid[0:CAL_COL_CNT,0:CAL_ROW_CNT].T.reshape(-1, 2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d points in real world space
imgpoints = [] # 2d points in image plane.

# Make a list of calibration images.
images = glob.glob('./camera_cal/calibration*.jpg')
img = None

# Step through the list and search for chessboard corners.
for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Find the chessboard corners.
    ret, corners = cv2.findChessboardCorners(gray, (CAL_COL_CNT,CAL_ROW_CNT), None)

    # If found, add object points, image points.
    if ret:
        objpoints.append(objp)
        imgpoints.append(corners)

        # Draw and display the corners.
        img = cv2.drawChessboardCorners(img, (CAL_COL_CNT,CAL_ROW_CNT), corners, ret)
        cv2.imshow('img', img)
        cv2.waitKey(500)

cv2.destroyAllWindows()

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, img.shape[1::-1], None, None)

cal_params = {'mtx': mtx, 'dist': dist}

# Pickle calibration params.
pickle.dump(cal_params, open('./camera_cal/calibration_params.p', 'wb'))
