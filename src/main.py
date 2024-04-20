import cv2
import numpy as np
import sys
import os
import re
from lib import parse_input_path, parse_options

def parse_args():
    ops = {"width":{"command": "-w", "default": "16"}, 
           "dest": {"command": "-d", "default": "./assets/dest"}, 
           "name": {"command": "-n", "default": "frame"}}
    
    argv = sys.argv

    input_path = parse_input_path(argv)
    option_value = parse_options(argv, ops)
    
    return (input_path, *option_value)

    

def main():
    input_path, size_str, dest, name = parse_args()
    size = int(size_str)

    if input_path[0] == "-":
        print("enter image path first")
        sys.exit(1)

    if size < 1:
        print("enter size more than 0")
        sys.exit(1)

    if not re.fullmatch(r"[-\w]+", name):
        print("enter valid file name")
        sys.exit(1)

    img = cv2.imread(input_path)
    if img is None:
        print('not correct path')
        sys.exit(1)

    h,w,c = img.shape
    img = np.hstack([np.zeros((h,size,3),dtype=np.uint8),img,np.zeros((h,size,3),dtype=np.uint8)])

    try :
        os.makedirs(dest, exist_ok=True)
    except Exception as e:
        print(e)
        sys.exit(1)

    for i in range(w+size):
        currentframe=img[:,i:i+size,:]
        cv2.imwrite(f"{dest}/{name}_{i}.bmp",currentframe)

if __name__ == "__main__":
    main()