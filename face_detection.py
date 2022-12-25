import cv2
from PIL import Image
import numpy as np


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


img = cv2.imread('test1.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.array(Image.open('test1.jpg').convert('L'), 'uint8')

faces = face_cascade.detectMultiScale(image=gray, minNeighbors=5, minSize=(20, 20), scaleFactor=1.1)


i = 1
for (x, y, w, h) in faces:
    cropped = img[y:y+h, x:x+w]
    cv2.imwrite(".\Faces\im" + str(i) + ".jpg", cropped)
    # cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    i += 1

cv2.imshow('img', img)
cv2.waitKey()
