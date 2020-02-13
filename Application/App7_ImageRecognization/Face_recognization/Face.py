import cv2

#Refer https://github.com/opencv/opencv/tree/master/data/haarcascades
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img=cv2.imread("Group1.jpeg")
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face=face_cascade.detectMultiScale(gray_img,
     scaleFactor=1.10,minNeighbors=5)

print(type(face))
print(face)
for x,y,w,h in face:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)



cv2.imshow("Grey",img)
cv2.waitKey(0)
cv2.destroyAllWindows()