import argparse
import cv2
import numpy as np
import sys
import os
import re

parser = argparse.ArgumentParser(description="指定した画像ファイルを任意のpxずつずらし、bmp画像にして出力する。")
parser.add_argument("input_path", type=str, help="指定する画像のパス。")
parser.add_argument("-u","--upright", action="store_true", help="指定した画像をずらす方向を定める。デフォルトは横向き、オプションを入れると縦向きになる。")
parser.add_argument("-r","--reverse", action="store_true", help="オプションを入れると指定した画像をずらす向きを逆転させる。")
parser.add_argument("-w","--width", type=int, default=320, help="出力する画像の幅。デフォルトは320px")
parser.add_argument("-i","--interval", type=int, default=1, help="出力する画像1枚ごとにずらすpx数。デフォルトは1px")
parser.add_argument("-d","--dest", type=str, default="./assets/dest", help="出力先のディレクトリ(指定したディレクトリが存在しない場合は作成される)。デフォルトはカレントディレクトリ内のassets/dest")
parser.add_argument("-n","--name", type=str, default="frame", help="出力する画像の名前。デフォルトはframe_数字.bmpで、frameの部分を変えられる。")
args = parser.parse_args()

# parserのtype=boolはだめらしいのでなんとかした

def main():
    input_path, size, interval, dest, name = args.input_path, args.width, args.interval, args.dest, args.name

    if size < 1:
        print("enter size more than 0")
        sys.exit(1)

    if interval < 1:
        print("enter interval more than 0")
        sys.exit(1)
    elif interval > size:
        print("enter interval less than width")
        sys.exit(1)

    if not re.fullmatch(r"[-\w]+", name):
        print("enter valid file name")
        sys.exit(1)

    img = cv2.imread(input_path)
    if img is None:
        print('not correct path')
        sys.exit(1)

    h,w,c = img.shape

    if args.upright:
        img = np.vstack([np.zeros((size,w,3),dtype=np.uint8),img,np.zeros((size,w,3),dtype=np.uint8)])
    else:
        img = np.hstack([np.zeros((h,size,3),dtype=np.uint8),img,np.zeros((h,size,3),dtype=np.uint8)])

    try :
        os.makedirs(dest, exist_ok=True)
    except Exception as e:
        print(e)
        sys.exit(1)

    if args.upright:
        start, i = 0, 0
        if args.reverse: start, interval = h+size-1, -interval
        while start < h + size and start >= 0:
            currentframe=img[start:start+size,:,:]
            cv2.imwrite(f"{dest}/{name}_{i}.bmp",currentframe)
            start += interval
            i += 1
    else:
        start, i = 0, 0
        if args.reverse: start, interval = w+size-1, -interval
        while start < w + size and start >= 0:
            currentframe=img[:,start:start+size,:]
            cv2.imwrite(f"{dest}/{name}_{i}.bmp",currentframe)
            start += interval
            i += 1

if __name__ == "__main__":
    main()
    