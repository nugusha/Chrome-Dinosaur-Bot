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
    
def imageGrab(start, coef1, coef2):
    X = Coordinates.dinosaur[0]
    Y = Coordinates.dinosaur[1]
    cc1 = Coordinates.c1
    cc2 = Coordinates.c2
    XX = (time.clock() - start)
    cc3 = coef1*XX + coef2 # Coordinates.c3[ind]
    if(XX>60.0):
        cc3 += 0.002*(XX-60)**(2.5)
    cc4 = Coordinates.c4
    box = (X+cc1, Y+cc2, X+cc3, Y+cc4)
    return imageGrabRect(box)

def imageGrabRect(box, gameover = False):
    image = ImageGrab.grab(box)
    
    arr = np.array(image)
    sh = arr.shape

    flag = 1
    count = 0
    flyDino = None
    cactus = None
    blackpixel = 0
    firstPixel = -1
    #if(gameover == False):
    #    print(box, arr.shape, " <==== ")
    for i,x in enumerate(arr):
        cactus = None
        for j, y in enumerate(x):
            if(y[0]<90 and y[1]<90 and y[2]<90):
                blackpixel += 1
                if(count == 0):
                    count += 1
                    firstPixel = j + Coordinates.c1
                    
                if(i==0):
                    flyDino = True
                cactus = True
                flag = 0
        
    if(gameover):
        return abs(blackpixel-67)<17

    if(flag == 1):
        return 0
                
    #print(box, sh[0], la, fi, firstPixel, gameover, flag, count)
    if(sh[0] == 30):
        
        if(cactus):
            if(firstPixel != -1):
                print(firstPixel, " abababababa <--==--")
                return (1, firstPixel)
            return 1

        if(flyDino):
            return 2
            
        return 0
    return 1
        
 
def gameEnded():
    #print(Coordinates.g)
    return imageGrabRect(Coordinates.g, True)

def saveScreenShot():
    pic = pyautogui.screenshot()
    #r = random.randint(100000, 999999)
    #pic.save('screenshot'+str(r)+'.png')