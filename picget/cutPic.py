#! /usr/bin python3


import sys
import argparse
import cv2  # opencv-python
import os


def video_to_frames(video, path_output_dir):
    # extract frames from a video and save to directory as 'x.png' where
    # x is the frame index
    vidcap = cv2.VideoCapture(video)
    count = 0
    while vidcap.isOpened():
        success, image = vidcap.read()
        if success:
            cv2.imwrite(os.path.join(path_output_dir, "%d.png") % count, image)
            count += 1
        else:
            break
    cv2.destroyAllWindows()
    vidcap.release()


# TODO:Interact with the command line(use argparse).
def main(argv=sys.argv[1:]):
    args = argparse.pase_args(argv)

    if args.command == "":
        pass


if __name__ == "__main__":
    video_to_frames("./test.mp4", "./out")
