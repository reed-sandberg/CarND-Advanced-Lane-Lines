#!/usr/bin/env python
# Copyright (C) 2016 Leapfin All Rights Reserved
"""
This script corrects sample images for camera distortion using calibration params.
"""

import glob
import pickle
import numpy as np

import cv2


# Load pickled calibration params.
cal_params = pickle.load(open('./camera_cal/calibration_params.p', 'rb'))
mtx = cal_params['mtx']
dist = cal_params['dist']

# Make a list of calibration images.
images = glob.glob('test_images/jobatest*.jpg') + glob.glob('camera_cal/calibration*.jpg')

# For each sample save an undistored version.
for fname in images:
    img = cv2.imread(fname)
    undist_img = cv2.undistort(img, mtx, dist, None, mtx)
    cv2.imwrite("{}-undist.jpg".format(fname.split('.')[0]), undist_img)
