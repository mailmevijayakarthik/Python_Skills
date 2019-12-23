import cv2

img=cv2.imread("Group1.jpeg",0)
print(img.shape)
print(img.ndim)
print(type(img))
print(img)

resized_img=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("Group",resized_img)
cv2.imwrite("Group_resize.jpg",resized_img)
print(img)
cv2.waitKey(0)
cv2.destroyAllWindows()

