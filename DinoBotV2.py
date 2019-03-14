from PIL import ImageGrab, ImageOps, Image
import pyautogui
import time
import numpy as np
from numpy import *

def addtoCoordinate(c, x, y, z, k):
    return (c[0]+x,c[1]+y,c[0]+z,c[1]+k)

class Coordinates():
    dinosaur = (160, 423)
    d = dinosaur
    replayBtn = (d[0]+180,d[1])
    flyingdino = addtoCoordinate(d, 60, -10, 100, -5)
    g = addtoCoordinate(d, 85, -55, 98, -43)
    c1 = 15
    c2 = 0
    #c3 = [100, 120, 120, 130, 130, 170, 210, 350]
    c4 = 25
    
class times():
    jumplen = [0.18, 0.18, 0.18, 0.17, 0.17, 0.17, 0.17, 0.17]
    lendlen = [0.15, 0.15, 0.14, 0.13, 0.12, 0.12, 0.11, 0.10]
    ducklen = [0.02, 0.018, 0.017, 0.015, 0.010, 0.010, 0.010, 0.010]
    timepassed = [10.0, 20.0, 30.0, 40.0, 70.0, 85.0, 100.0, 1000.0]

start = 0.0
 
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
    
def imageGrab(ind, box=True):
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
    
def main():
    '''
    last = None
    ccc = 0
    while(True):
        if(last!=pyautogui.position()):
            print(pyautogui.position())
        last=pyautogui.position()
        ccc += 1
        if(ccc == 10):
            break
        pyautogui.click(Coordinates.dinosaur)
        pyautogui.click((Coordinates.g[2],Coordinates.g[3]))
        pyautogui.click(Coordinates.replayBtn)
    while(True):
        continue
    '''
 
    a=0
    b=0
    global start
    start = time.clock()
    end = None
    restartGame()
    while(True):    
        timelen = time.clock() - start
        for i,t in enumerate(times.timepassed):
            if(timelen<t):
                ind = i
                break
 
        if(imageGrabRect(Coordinates.g, True)==True):
            pyautogui.click((1000,500))
            
            end = time.clock()
            print(end - start, ind)
            time.sleep(3.0)
            pic = pyautogui.screenshot()
            r = random.randint(100000, 999999)
            pic.save('screenshot'+str(r)+'.png')
                
            restartGame()
            start = time.clock()
            continue
            
        #print(a-b)
        #a = time.time()
        res = imageGrab(ind)
        #b = time.time()
        #print(b-a)
        if(res == 1):
            press('space', ind)
        elif(res == 2):
            press('down', ind)
main()