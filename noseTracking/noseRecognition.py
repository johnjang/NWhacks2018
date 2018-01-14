import numpy as np
import cv2
import tkinter as tk

root = tk.Tk()
erase = False
draw = False
counter = 0
prevcenter = (0, 0)
depth = 40

def run(x, y, w, h):
    global erase, draw, counter, prevcenter
    length = 512
    width = 512
    img = np.zeros((length, width, 3), np.uint8)

    nose_cascade = cv2.CascadeClassifier('haarcascade_mcs_nose.xml')
    cp = [x + w / 2, y + h / 2]

    old_w = w
    new_w = 0
    radius = 5

    while (cap.isOpened()):

        ret, frame = cap.read()

        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = cv2.flip(gray, 1)
            nose = nose_cascade.detectMultiScale(gray, 1.3, 5)

            for (ex, ey, ew, eh) in nose:
                new_w = ew
                if ((abs((ex + ew / 2) - cp[0]) > 5 or abs((ey + eh / 2) - cp[1]) > 5) and (
                        abs((ex + ew / 2) - cp[0]) < 15 or abs((ey + eh / 2) - cp[1]) < 15)):
                    cp = [ex + ew / 2, ey + eh / 2]

            center = (int(cp[0]), int(cp[1]))

            cv2.namedWindow('img', cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty('img',
                                  cv2.WND_PROP_FULLSCREEN,
                                  cv2.WINDOW_FULLSCREEN)

            cv2.imshow('img', img)

            if(new_w > old_w):
                radius += 5
            elif(new_w < old_w and radius > 10):
                radius -= 10

            old_w = new_w

            print(radius)
            if erase:
                cv2.line(img, prevcenter, center, (0, 0, 0), thickness=20, lineType=8)
            elif draw:
                cv2.line(img, prevcenter, center, (0, 255, 0), thickness=radius, lineType=8)
            else:
                cv2.circle(img, center, 5, (0, 0, 255), -1)
                if (counter % 2 == 0):
                    img = np.zeros((length, width, 3), np.uint8)

            prevcenter = center
            counter += 1

            k = cv2.waitKey(1) & 0xFF
            if k == ord("e"):
                erase = True
                draw = False
            if k == ord("c"):
                draw = False
                erase = False
                img = np.zeros((length, width, 3), np.uint8)
            if k == 32:
                draw = not draw
                erase = False
            if k == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FPS, 10)

    nose_cascade = cv2.CascadeClassifier('haarcascade_mcs_nose.xml')
    radius = 3

    while (cap.isOpened()):
        ret, frame = cap.read()

        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            nose = nose_cascade.detectMultiScale(gray, 1.3, 5)

            new_x = 0
            new_y = 0
            new_w = 0
            new_h = 0
            for (x, y, w, h) in nose:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                new_x = x
                new_y = y
                new_w = w
                new_h = h
                cv2.circle(frame, (int(x + w / 2), int(y + h / 2)), abs(depth - w), (255, 0, 0), -1)

            cv2.namedWindow('frame', cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty('frame',
                                  cv2.WND_PROP_FULLSCREEN,
                                  cv2.WINDOW_FULLSCREEN)
            frame = cv2.flip(frame, 1)
            cv2.imshow('frame', frame)
            k = cv2.waitKey(1) & 0xFF

            if k == ord("e"):
                run(new_x, new_y, new_w, new_h)
            if (k == ord("q")):
                break
