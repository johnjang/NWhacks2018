import numpy as np
import cv2

def run(x, y, w, h):
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FPS, 30)

    nose_cascade = cv2.CascadeClassifier('haarcascade_mcs_nose.xml')
    cp = [(x+w)/2, (y+h)/2]
    while (cap.isOpened()):

        ret, frame = cap.read()

        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            nose = nose_cascade.detectMultiScale(gray, 1.3, 5)

            for (ex, ey, ew, eh) in nose:
                if((abs(((ex+ew)/2)-cp[0]) > 2 or abs(((ey+eh)/2)-cp[1]) > 2) or (abs(((ex+ew)/2)-cp[0]) < 20 or abs(((ey+eh)/2)-cp[1]) < 20)):
                    cp = [(ex+ew)/2, (ey+eh)/2]

            print(cp[0], cp[1])
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FPS, 10)

    nose_cascade = cv2.CascadeClassifier('haarcascade_mcs_nose.xml')
    while (cap.isOpened()):
        ret, frame = cap.read()

        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            nose = nose_cascade.detectMultiScale(gray, 1.3, 5)

            nx = 0
            ny = 0
            nw = 0
            nh = 0
            for (x, y, w, h) in nose:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                nx = x
                ny = y
                nw = w
                nh = h

            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('e'):
                break

    cap.release()
    cv2.destroyAllWindows()
    run(nx, ny, nw, nh)
