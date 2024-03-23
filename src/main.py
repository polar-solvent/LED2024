import cv2
import numpy as np
import sys
import os
import re

def options():
    ops = {"width":{"command": "-w", "default": 16}, 
           "dest": {"command": "-d", "default": "./assets/dest"}, 
           "name": {"command": "-n", "default": "frame"}}
    argv = sys.argv
    length = len(argv)
    if length == 1:
        print('no image path')
        sys.exit(1)
    input_path = argv[1]
    opdict = [{"option" : argv[2::2][x], "value" : argv[3::2][x]} for x in range(int(length/2-1))]
    if length > 2+2*len(ops):
        print("too much options or miss space")
        sys.exit(1)
    oplist_original = [dct.get("option") for dct in opdict]
    oplist = [op if len(op) == 2 else op[1:3] for op in oplist_original]
    if len(set(oplist)) != len(oplist):
        print("enter one option only once")
        sys.exit(1)
    for op in ops.values():
        try:
            opindex = oplist.index(op["command"])
        except ValueError:
            continue
        op["default"] = opdict[opindex]["value"]
    return (input_path, *[dct.get("default") for dct in ops.values()])

def main():
    input_path, size_str, dest, name = options()
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