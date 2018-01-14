import numpy as np
import cv2

erase = False
draw = False
counter = 0 
prevcenter = (0,0)
def run(x, y, w, h):
    global erase, draw, counter ,prevcenter
    length = 512
    width = 512
    img = np.zeros((length,width,3), np.uint8)
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
            center = (length -int(cp[0]),int(cp[1]))

            cv2.namedWindow('img', cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty('img',
                              cv2.WND_PROP_FULLSCREEN,
                              cv2.WINDOW_FULLSCREEN)

            cv2.imshow('img',img)


            if erase:
                #cv2.circle(img,center,5,(0,0,0),-1)
                #erase lines from previous center to current center
                cv2.line(img, prevcenter, center, (0, 0, 0), thickness=3, lineType=8)
            elif draw:
                #cv2.circle(img,center,5,(0,255,0),-1)
                #draw lines from revious center to current center
                cv2.line(img, prevcenter, center, (0, 255, 0), thickness=3, lineType=8)
            else:
                cv2.circle(img,center,5,(0,0,255),-1)
                if(counter%2 == 0):
                    img = np.zeros((length,width,3), np.uint8)
            prevcenter = center
            counter += 1
            k = cv2.waitKey(1) & 0xFF
            if k == ord("e"):
                erase = True
                draw = False
            if k == ord("c"):
                draw = False
                erase = False
                img = np.zeros((length,width,3), np.uint8)
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
                cv2.circle(frame,(int(x+w/2),int(y+h/2)), 5,(255,0,0),-1)
            cv2.namedWindow('frame', cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty('frame',
                              cv2.WND_PROP_FULLSCREEN,
                              cv2.WINDOW_FULLSCREEN)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('e'):
                break

    cap.release()
    cv2.destroyAllWindows()
    run(nx, ny, nw, nh)
