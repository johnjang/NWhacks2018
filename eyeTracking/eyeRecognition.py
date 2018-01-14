import numpy as np
import cv2

cap = cv2.VideoCapture(0)

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

while(cap.isOpened()):

    ret, frame = cap.read()

    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)

        sumx = 0
        sumy = 0
        sumew =0
        sumeh =0
        for (ex, ey, ew, eh) in eyes:
            if(ex < sumx):
                sumx = ex
                sumy = ey
            sumew = sumew + ew
            sumeh = sumeh + eh

        sumx = int(sumx)
        sumy = int(sumy)
        sumew = int(sumew / 2)
        sumeh = int(sumeh / 2)

        cv2.rectangle(frame,(sumx,sumy),(sumx+3*sumew, sumy + sumeh),(0,255,0),2)
        roi_gray2 = gray[sumy:sumy + sumeh, sumx:sumx + sumew]
        roi_color2 = frame[sumy:sumy + sumeh, sumx:sumx + sumew]
        # circles = cv2.HoughCircles(roi_gray2, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
        print(sumx, sumy)

        # for (ex,ey,ew,eh) in eyes:
        #     cv2.rectangle(frame,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        #     roi_gray2 = gray[ey:ey+eh, ex:ex+ew]
        #     roi_color2 = frame[ey:ey+eh, ex:ex+ew]
        #     circles = cv2.HoughCircles(roi_gray2,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
        #     print(ex,ey)
            #try:
                #for i in circles[0,:]:
                # draw the outer circle
                    #cv2.circle(roi_color2,(i[0],i[1]),i[2],(255,255,255),2)
                    #print(i[0])
                    #print(i[1])
                    #print("drawing circle")
                # draw the center of the circle
                    #cv2.circle(roi_color2,(i[0],i[1]),2,(255,255,255),3)
            #except Exception as e:
             #   print(e)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
