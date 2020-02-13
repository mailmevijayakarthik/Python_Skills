import cv2
import sys
class face_scrapper:

    def ExtractFacefromImage(self,img):

        image=cv2.imread(img)
        gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        #face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

        faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.10,
                minNeighbors=3,
                minSize=(30, 30)
        )

        print("[INFO] Found {0} Faces!".format(len(faces)))

        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            roi_color = image[y:y + h, x:x + w]
            print("[INFO] Object found. Saving locally.")
            cv2.imwrite("/Users/vijayakarthikeyanarul/git/python_Skills/Application/App7_ImageRecognization/Face_scrapper/Resources/"+str(w) + str(h) + '_faces.jpg', roi_color)

        status = cv2.imwrite('faces_detected.jpg', image)
        print("[INFO] Image faces_detected.jpg written to filesystem: ", status)

    def capturefaceinVideo(self, video):
        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        a = 1
        while True:
            a = a + 1
            check, frame = video.read()
            print(check)

            face = face_cascade.detectMultiScale(frame,
                                                 scaleFactor=1.10, minNeighbors=5)
            for x, y, w, h in face:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                roi_color = frame[y:y + h, x:x + w]
                print("[INFO] Object found. Saving locally.")
                cv2.imwrite(
                    "/Users/vijayakarthikeyanarul/git/python_Skills/Application/App7_ImageRecognization/Face_scrapper/Resources/" + str(
                        w) + str(h) + '_faces.jpg', roi_color)

            print("Face : ", face)
            print("Frame :", frame)

            # time.sleep(1)
            cv2.imshow("Capturing video..", frame)
            key = cv2.waitKey(1000)
            if key == ord('q'):
                break
        print("Number of Frames ", a)

face_input=face_scrapper()
face_input.ExtractFacefromImage("Group1.jpeg")
# vid = cv2.VideoCapture(0)
# face_input.capturefaceinVideo(vid)
# vid.release()
#
# cv2.destroyAllWindows()
