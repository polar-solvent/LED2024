import cv2

img = cv2.imread("./assets/rapid.bmp")
for _ in range(12):
    a = img[:,0,:]
    img[:,:-1,:] = img[:,1:,:]
    img[:,-1,:] = a
cv2.imshow("image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()