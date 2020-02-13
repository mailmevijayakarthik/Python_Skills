import cv2
import glob
import os

images=glob.glob("resized_Group1.jpeg")

print(os.getcwd())

for image in images:
    img=cv2.imread(image,0)
    #re=cv2.resize(img,(100,100))
    re=cv2.resize(img,(280,850))
    cv2.imshow("Hey",re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+image,re)