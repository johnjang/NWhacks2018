import cv2
import numpy as np

draw = False
length = 512
width = 512
# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_MOUSEMOVE:
        if draw:
            cv2.circle(img,(x,y),5,(255,0,0),-1)

# Create a black image, a window and bind the function to window
img = np.zeros((length,width,3), np.uint8)
cv2.namedWindow('image')
# mouse call back instead just input x,y
cv2.setMouseCallback('image',draw_circle)

while(1):
    k = cv2.waitKey(1) & 0xFF
    cv2.imshow('image',img)
    if k == ord("c"):
        img = np.zeros((length,width,3), np.uint8)
    if k == 32:
        draw = not draw
    if k == 27:
        break
cv2.destroyAllWindows()
