import cv2
import numpy as np


def main():
    SIZE = 16
    img = cv2.imread("./assets/src/rapid.bmp")
    h,w,c = img.shape
    img = np.hstack([np.zeros((h,SIZE,3),dtype=np.uint8),img,np.zeros((h,SIZE,3),dtype=np.uint8)])
    for i in range(w+SIZE):
        currentframe=img[:,i:i+SIZE,:]
        cv2.imwrite(f"./assets/dest/frame_{i}.bmp",currentframe)