# openCV color space conversion into Gray/HSV, and converted from Gray/HSV to RGB
import cv2

img = cv2.imread('test.jpg')
gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print(type(gray))
print(gray.shape)
print(gray)
cv2.imshow('ORG' ,img)
cv2.imshow('GRAY',gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
