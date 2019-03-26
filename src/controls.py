import pyautogui
import time
from PIL import ImageGrab, ImageOps, Image
import numpy as np
from Coordinates import *
def restartGame():
     pyautogui.click(Coordinates.replayBtn)

def press(st,ind):
    pyautogui.keyDown(st)
    twodino = Coordinates.d + Coordinates.d
    if(st == 'space'):
        time.sleep(times.lendlen[ind])
        head = addtoCoordinate(twodino,0,20,50,21)
        
        if(imageGrabRect(head)==False):
            pyautogui.keyDown('down')
            time.sleep(times.ducklen[ind])
            pyautogui.keyUp('down')
    else:
        head = addtoCoordinate(twodino,-50,0,135,1)
        while(imageGrabRect(head)):
            continue
    pyautogui.keyUp(st)
    
def imageGrab(ind, box=True, start = 0.0):
    if(box==True):
        X = Coordinates.dinosaur[0]
        Y = Coordinates.dinosaur[1]
        cc1 = Coordinates.c1
        cc2 = Coordinates.c2
        XX = (time.clock() - start)
        cc3 = 1.1*XX + 110 # Coordinates.c3[ind]
        if(XX>60.0):
            #cc3 += 0.026*(XX-60)**(1.8)
            cc3 += 0.002*(XX-60)**(2.5)
        cc4 = Coordinates.c4
        box = (X+cc1, Y+cc2, 
            X+cc3, Y+cc4)
        return imageGrabRect(box)

def imageGrabRect(box, gameover = False):
    image = ImageGrab.grab(box)
    
    arr = np.array(image)
    sh = arr.shape

    flag = 1
    count = 0
    fi = None
    la = None
    blackpixel = 0
    for x in arr:
        la = None
        for y in x:
            if(y[0]<90 and y[1]<90 and y[2]<90):
                blackpixel += 1
                if(count == 0):
                    fi = True
                la = True
                flag = 0
        count += 1

    if(gameover == True):
        return abs(blackpixel-67)<17

    if(flag == 1):
        return False
                
    if(sh[0] == 25):
        
        if(la == True):
            return 1

        if(fi == True):
            return 2
            
        return 0
                 
    return (flag == 0)

def gameEnded():
    return imageGrabRect(Coordinates.g, True)

def saveScreenShot():
    pic = pyautogui.screenshot()
    #r = random.randint(100000, 999999)
    #pic.save('screenshot'+str(r)+'.png')