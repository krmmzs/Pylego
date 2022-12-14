#! /usr/bin python3


import sys
import cv2  # opencv-python
import os
from plyer import notification


def video_to_frames(video, path_output_dir):
    """
    extract frames from a video and save to directory as 'x.png' where
    x is the frame index

    Keyword arguments:
    video -- video source
    path_output_dir -- the path output dir
    """
    try:
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
        notification.notify(
            title="Finished executing " + sys.argv[0],
            message="Successful",
        )
    except Exception as e:
        notification.notify(
            title="Finished executing " + sys.argv[0],
            message="Failed",
        )
        raise e


def main(argv=sys.argv[1:]):
    src = argv[0]
    out = argv[1]
    video_to_frames(src, out)


if __name__ == "__main__":
    main()
