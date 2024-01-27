import cv2
import numpy as np

SIZE = 16
img = cv2.imread("./assets/src/rapid.bmp")
h,w,c = img.shape
img = np.hstack([np.zeros((h,SIZE,3),dtype=np.uint8),img,np.zeros((h,SIZE,3),dtype=np.uint8)])
for i in range(w+SIZE):
    currentframe=img[:,i:i+SIZE,:]
    cv2.imshow("image",currentframe)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(f"./assets/dest/frame_{i}.bmp",currentframe)