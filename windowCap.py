import numpy as np
import cv2
from PIL import ImageGrab
import time
from ctypes import windll
from numpy import *
import pyautogui

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
dino_cascade = cv2.CascadeClassifier('cascade_Final_Dino.xml')
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
cact_cascade = cv2.CascadeClassifier('cascade_Final_Cactus.xml')

#cap = cv2.VideoCapture(0)

def drawrect(obj, img, color):
    dx = 0
    dy = 0
    dw = 0
    dh = 0
    dim = [dx,dy,dw,dh]
    for (x,y,w,h) in obj:
        cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
        dx = x
        dim = [dx,dy,dw,dh]
    return dim
        
lowest_cx = [1920,0,0,0]
dx = [0,0,0,0]
cx = [1920,0,0,0]
while(True):
    #ret, img = printscreen_numpy.read()
    blue = (0,0,255)
    red = (255,0,0)
    green = (0,255,0)
    printscreen_pil =  ImageGrab.grab()
    printscreen_numpy =   np.array(printscreen_pil, dtype="uint8")\
    .reshape((printscreen_pil.size[1],printscreen_pil.size[0],3)) 
    img = printscreen_numpy
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    dinos = dino_cascade.detectMultiScale(gray, 1.2, 5)
    dx = drawrect(dinos, img, blue)
    cacts = cact_cascade.detectMultiScale(gray, 1.2, 5)
    cx = drawrect(cacts, img, green)
    
    if cx[0] <= lowest_cx[0]:
        lowest_cx = cx
    if cx[0] is 0:
        lowest_cx[0] = 1920
        
    #print(lowest_cx[0], cx[0], dx[0])
    if (dx[0]+dx[2]+5) >= lowest_cx[0]:
        print("jump")
        pyautogui.press('space')
        lowest_cx[0] = 1920
        

    


    cv2.imshow('img',img)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
cap.release()
cv2.destroyAllWindows()
