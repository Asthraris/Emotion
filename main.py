import cv2 as cv
from deepface import DeepFace

video = cv.VideoCapture(0)

face_cascd = cv.CascadeClassifier( "cascades/haarcascade_frontalface_default.xml")

while True:
    #
    ret,frame = video.read()
    if not ret:
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascd.detectMultiScale(gray,scaleFactor=1.3 , minNeighbors=4)
    if len(faces)>0:
        try:
            predictions = DeepFace.analyze(frame , actions=["emotion"])

            for i ,(x,y,w,h)in enumerate(faces):
                cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                if isinstance(predictions, list):
                    emotion = predictions[i]['dominant_emotion']
                else:
                    emotion = predictions['dominant_emotion']
                cv.putText(frame, emotion, (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        except Exception as e:
            print("Failed:",e)


    cv.imshow("Emotion detection",frame)
    if cv.waitKey(1) & 0xFF==ord('q'):
        break

video.release()
cv.destroyAllWindows()

