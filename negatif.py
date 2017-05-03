import numpy as np
import cv2

cap = cv2.VideoCapture(0) #ntuk melakukan perintah membuka webcam. karakter "0" mewakili webcam internal pada pc.
print(cap.isOpened())

while(True): #program untuk looping imshow, camera akan menangkap objek bergerak secara realtime.
    ret, frame = cap.read() #menampilkan citra dengan format BGR
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #mengkonversi citra menjadi skala abu abu (grayscale)
    cv2.imshow('webcam', 255-gray) # menampilkan citra grayscale yang dikonversi menjadi negatif. 
    if cv2.waitKey(1) == 27: #perintah untuk menghentikan program dengan menekan tombol esc pada keyboard. key 27 adalah nomor tombol dari esc
        break


cap.realease()
cv2.destroyAllwindows()
