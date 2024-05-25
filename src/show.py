import argparse
import sys
import os
import re
import cv2

parser = argparse.ArgumentParser(description="画像群を読み込み、末尾の数字の順番通りに一定の速さで表示する。qを押すと終了する。")
parser.add_argument("input_path", type=str, help="表示する画像群のパス。一つの画像のパスを入力すればよい。")
parser.add_argument("-s","--speed", type=int, default=60, help="表示するときの、次の画像へ移る速さ。デフォルトは60fps。数字が大きいほど速い。")
args = parser.parse_args()
    
def main():
    input_path, speed = args.input_path, args.speed

    if speed < 1:
        print("enter frame rate more than 0")
        sys.exit(1)

    elif speed > 1000:
        print("enter frame rate less than 1000")
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
        print("no such frames in this directory")
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

        if cv2.waitKey(wait_ms) == ord("q"):
            break

    cv2.destroyAllWindows()
    