import cv2, time


class MyVideo():

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
                frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

            print("Face : ", face)
            print("Frame :", frame)

            # time.sleep(1)
            cv2.imshow("Capturing video..", frame)
            key = cv2.waitKey(1000)
            if key == ord('q'):
                break
        print("Number of Frames ", a)

    def generateImagefromVideo(self, video):
        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        b = 0
        while True:
            b = b + 1
            success, image = video.read()
            gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            face = face_cascade.detectMultiScale(gray_img,
                                                 scaleFactor=1.10, minNeighbors=5)
            for x, y, w, h in face:
                image = cv2.rectangle(gray_img, (x, y), (x + w, y + h), (0, 255, 0), 3)

            cv2.imwrite("frame%d.jpg" % b, image)
            print("Face : ", face)
            print("Frame :", image)
            cv2.imshow("Capturing Image ..", image)
            key = cv2.waitKey(1000)
            if key == ord('q'):
                break
        print("Number of Images :", b)


myvideo = MyVideo()
video = cv2.VideoCapture(0)
myvideo.capturefaceinVideo(video)
# myvideo.generateImagefromVideo(video)
video.release()
cv2.destroyAllWindows()
