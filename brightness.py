import numpy as np
import cv2

cap = cv2.VideoCapture(0) #ntuk melakukan perintah membuka webcam. karakter "0" mewakili webcam internal pada pc.
print(cap.isOpened())


while(True): #program untuk looping imshow, camera akan menangkap objek bergerak secara realtime.
    ret, frame = cap.read() #menampilkan citra dengan format BGR
    bright = cv2.addWeighted(frame,1.5, np.zeros(frame.shape, frame.dtype), 0, 25) #untuk meningkatkan nilai kecerahan citra
    cv2.imshow('webcam',bright) #untuk menampilkan citra yang tellah diubah tingkat kecerahannya.
    if cv2.waitKey(1) == 27: #perintah untuk menghentikan program dengan menekan tombol esc pada keyboard. key 27 adalah nomor tombol dari esc
        break


cap.realease()
cv2.destroyAllwindows()
