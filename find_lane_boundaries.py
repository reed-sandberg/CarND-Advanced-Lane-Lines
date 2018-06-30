#!/usr/bin/env python
#
# Identify and draw our lane and expected path of travel.

from moviepy.editor import VideoFileClip

from zone import LaneBoundaryZone

def main():
    """Start here..."""

    # project_video.mp4
    project_video = VideoFileClip('./project_video.mp4')
    sample_img = project_video.get_frame(0)
    zone = LaneBoundaryZone(sample_img.shape[0], sample_img.shape[1])
    project_video_lane = project_video.fl_image(zone.locate_lane_bounds)
    project_video_lane.write_videofile('./output_videos/project_video_lane.mp4', audio=False)

    # challenge_video.mp4
    challenge_video = VideoFileClip('./challenge_video.mp4')
    sample_img = challenge_video.get_frame(0)
    zone = LaneBoundaryZone(sample_img.shape[0], sample_img.shape[1])
    zone.hough_threshold = 39
    zone.v_thresh_min = 165
    zone.s_thresh_min = 51
    zone.min_lane_slope = 0.6
    zone.y_thresh_min = 12
    zone.x_thresh_min = 8
    zone.min_windows_per_lane = 2
    zone.combine_pipeline_method = 'or_related_and_groups'
    challenge_video_lane = challenge_video.fl_image(zone.locate_lane_bounds)
    challenge_video_lane.write_videofile('./output_videos/challenge_video_lane.mp4', audio=False)

    # harder_challenge_video.mp4
    harder_challenge_video = VideoFileClip('./harder_challenge_video.mp4')
    sample_img = harder_challenge_video.get_frame(0)
    zone = LaneBoundaryZone(sample_img.shape[0], sample_img.shape[1])
    zone.hough_threshold = 39
    zone.v_thresh_min = 246
    zone.s_thresh_min = 73
    zone.min_lane_slope = 0.3
    zone.y_thresh_min = 21
    zone.x_thresh_min = 24
    zone.min_windows_per_lane = 2
    zone.min_lane_line_cluster_size = 7
    zone.horizon_frame_smooth_size = 6
    zone.lane_find_window_height = 10
    zone.lane_find_margin = 10
    zone.proportion_image_height_levels = 0.33
    zone.lane_curve_radius_min = 0
    zone.lane_diverge_max = 0.15
    zone.min_inverse_noise_factor = 5000
    zone.combine_pipeline_method = 'and_related_or_groups'
    harder_challenge_video_lane = harder_challenge_video.fl_image(zone.locate_lane_bounds)
    harder_challenge_video_lane.write_videofile('./output_videos/harder_challenge_video_lane.mp4', audio=False)

if __name__ == '__main__':
    main()
