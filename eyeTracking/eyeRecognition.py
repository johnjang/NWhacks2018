import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 10)

nose_cascade = cv2.CascadeClassifier('haarcascade_mcs_nose.xml')

while(cap.isOpened()):

    ret, frame = cap.read()

    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        nose = nose_cascade.detectMultiScale(gray, 1.3, 5)

        sumx = 0
        sumy = 0
        sumew =0
        sumeh =0
        for (ex, ey, ew, eh) in nose:
            if(ex != sumx):
                sumx = ex
                sumy = ey
            sumew = sumew + ew
            sumeh = sumeh + eh

        sumx = int(sumx)
        sumy = int(sumy)
        sumew = int(sumew)
        sumeh = int(sumeh)

        cv2.rectangle(frame,(sumx,sumy),(sumx+sumew, sumy+sumeh),(0,255,0),2)
        roi_gray2 = gray[sumy:sumy + sumeh, sumx:sumx + sumew]
        roi_color2 = frame[sumy:sumy + sumeh, sumx:sumx + sumew]
        print(sumx, sumy)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
