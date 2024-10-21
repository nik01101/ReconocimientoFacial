import cv2
import numpy as np
import face_recognition

img1 = face_recognition.load_image_file("ImagenesRostros/manroca.jpg")
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = face_recognition.load_image_file("ImagenesRostros/giuliano.jpg")
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

faceLocM = face_recognition.face_locations(img1)[0]
encodeImg1 = face_recognition.face_encodings(img1)[0]
cv2.rectangle(img1,(faceLocM[3], faceLocM[0]),(faceLocM[1], faceLocM[2]),(0,255,0),2)

faceLocG = face_recognition.face_locations(img2)[0]
encodeImg2 = face_recognition.face_encodings(img2)[0]
cv2.rectangle(img2,(faceLocG[3], faceLocG[0]),(faceLocG[1], faceLocG[2]),(0,255,0),2)

results = face_recognition.compare_faces([encodeImg1],encodeImg2)
faceDis = face_recognition.face_distance([encodeImg1],encodeImg2)
print(results,faceDis)
cv2.putText(img2,f'{results} {round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

cv2.imshow("Manroca", img1)
cv2.imshow("Giuliano", img2)
cv2.waitKey(0)
