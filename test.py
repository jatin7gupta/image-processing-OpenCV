import cv2
img = cv2.imread('COMP9517_20T2_Assignment_Images/Particles.png', 1)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()