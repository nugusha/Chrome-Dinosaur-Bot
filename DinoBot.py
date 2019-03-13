from PIL import ImageGrab, ImageOps, Image
import pyautogui
import time
import numpy as np
from ctypes import windll
from numpy import *
class consts():
    gameoverCNT = 2634
    gameoverCNTLet = 474
    flyingdino = 447

po = 1

def addtoCoordinate(c, x, y, z, k):
    return (c[0]+x,c[1]+y,c[0]+z,c[1]+k)

class Coordinates():
    dinosaur = (174, 423)
    d = dinosaur
    replayBtn = (d[0]+150,d[1]-25)
    flyingdino = addtoCoordinate(d, 60, -10, 100, -5)
    g = addtoCoordinate(d, 73, -55, 84, -43)
    c1 = [15, 15, 15, 15, 15, 15, 15]
    c2 = [0, 0, 0, 0, 0, 0, 0]
    c3 = [100, 120, 120, 130, 130, 170, 210]
    c4 = [25, 25, 25, 25, 25, 25, 25]
    
class times():
    jumplen = [0.18, 0.18, 0.18, 0.17, 0.17, 0.17, 0.17]
    timepassed = [10.0, 20.0, 30.0, 40.0, 70.0, 85.0, 1000.0]

def restartGame():
    pyautogui.click(Coordinates.replayBtn)

def press(st,ind):
    pyautogui.keyDown(st)
    if(st == 'space'):
        time.sleep(times.jumplen[ind])
    else:
        twodino = Coordinates.d + Coordinates.d
        head = addtoCoordinate(twodino,-50,0,135,1)
        #print(head)
        while(imageGrabRect(head)):
            continue
    pyautogui.keyUp(st)
    
def imageGrab(ind, box=True):
    if(box==True):
        X = Coordinates.dinosaur[0]
        Y = Coordinates.dinosaur[1]
        cc1 = Coordinates.c1[ind]
        cc2 = Coordinates.c2[ind]
        cc3 = Coordinates.c3[ind]
        cc4 = Coordinates.c4[ind]
        box = (X+cc1, Y+cc2, 
            X+cc3, Y+cc4)
        return imageGrabRect(box)

def imageGrabRect(box):
    image = ImageGrab.grab(box)
    
    arr = np.array(image)
    sh = arr.shape
    #height, width  = sh[0], sh[1]

    #if(a.sum()!=447):
    #    print(arr)

    flag = 1
    obs = 0
    count = 0
    fi = None
    la = None
    for x in arr:
        la = None
        for y in x:
            if(y[0]<90 and y[1]<90 and y[2]<90):
                if(count == 0):
                    fi = True
                la = True
                obs += 1
                flag = 0
        count += 1
    '''
    print("----------")
    print(fi)
    print(la)

    print("====")
    uuuu = input()
    '''

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
    while(True):
        print(imageGrab(0))
        print(imageGrab(1))
        print(imageGrab(2))
        print(imageGrab(3))
        u = input()
    '''

    #print(imageGrabRect(addtoCoordinate(Coordinates.d,60,-5,100,0)))
    
    '''
    last = None
    while(True):
        if(last!=pyautogui.position()):
            print(pyautogui.position())
        last=pyautogui.position()
    '''

    a=0
    b=0
    start = time.clock()
    end = None
    cnt = 0
    restartGame()
    while(True):    
        timelen = time.clock() - start
        for i,t in enumerate(times.timepassed):
            if(timelen<t):
                ind = i
                break

        #print(Coordinates.g)
        #print(Coordinates.gameover," <==")
            
        if(imageGrabRect(Coordinates.g)==True):
            
            end = time.clock()    
            print(end - start, ind)
            time.sleep(3.0)
            pic = pyautogui.screenshot()
            #r = random.randint(100000, 999999)
            #pic.save('screenshot'+str(r)+'.png')

            #cnt += 1
            #if(cnt == 100):
            #    break
                
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
            #print(res)
            press('down', ind)
main()