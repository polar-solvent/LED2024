import os
import re
import cv2
import time

dir_path = "assets/dest"
def is_frame(f):
    return re.match(r"frame_\d+\.bmp", f)

frames_name = [
    f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f)) and is_frame(f)
]

def sort_frame(f):
    m = re.match(r"frame_(\d+)\.bmp", f)
    return int(m.group(1))

frames_name_sorted = sorted(frames_name,key=sort_frame)

cv2.namedWindow("image")

frames = [cv2.imread(f"./assets/dest/{f}") for f in frames_name_sorted]
    
st = time.perf_counter()

for f in frames:
    cv2.imshow("image", f)

    cv2.waitKey(10)

ed = time.perf_counter()

cv2.destroyAllWindows()

print(ed - st)