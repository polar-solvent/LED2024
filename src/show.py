import sys
import os
import re
import cv2
from lib import parse_input_path, parse_options

def parse_args():
    ops = {"speed": {"command": "-s", "default": "60"}}

    argv = sys.argv

    input_path = parse_input_path(argv)
    option_value = parse_options(argv, ops)
    
    return (input_path, *option_value)
    
def main():
    input_path, speed_str = parse_args()

    speed = int(speed_str)

    if speed < 1:
        print("enter frame rate more than 0")
        sys.exit(1)

    dir_path, frame_name_original= os.path.split(input_path)
    underscore_index = frame_name_original.rindex("_")
    frame_name = frame_name_original[:underscore_index]
    
    def is_frame(f:str):
        return re.match(rf"{frame_name}_\d+\.bmp", f)

    frames_name = [
        f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f)) and is_frame(f)
    ]

    if frames_name == []:
        print("no frames here")
        sys.exit(1)

    def sort_frame(f:str):
        m = re.match(rf"{frame_name}_(\d+)\.bmp", f)
        return int(m.group(1))

    frames_name_sorted = sorted(frames_name,key=sort_frame)

    cv2.namedWindow("image")

    frames = [cv2.imread(rf"{dir_path}/{f}") for f in frames_name_sorted]

    wait_ms = 1000//speed

    for f in frames:
        cv2.imshow("image", f)

        cv2.waitKey(wait_ms)

    cv2.destroyAllWindows()