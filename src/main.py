import argparse
import cv2
import numpy as np
import sys
import os
import re

parser = argparse.ArgumentParser(description="指定した画像ファイルを1pxずつずらし、bmp画像にして出力する。")
parser.add_argument("input_path", type=str, help="指定する画像のパス。")
parser.add_argument("-w","--width", type=int, default=320, help="出力する画像の横幅。デフォルトは320px")
parser.add_argument("-d","--dest", type=str, default="./assets/dest", help="出力先のディレクトリ(指定したディレクトリが存在しない場合は作成される)。デフォルトはカレントディレクトリ内のassets/dest")
parser.add_argument("-n","--name", type=str, default="frame", help="出力する画像の名前。デフォルトはframe_数字.bmpで、frameの部分を変えられる。")
args = parser.parse_args()

def main():
    input_path, size, dest, name = args.input_path, args.width, args.dest, args.name

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