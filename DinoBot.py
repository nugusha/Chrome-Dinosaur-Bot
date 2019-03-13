from PIL import ImageGrab, ImageOps, Image
import pyautogui
import time
import numpy as np
from numpy import *
class consts():
    obstacles = [447, 447, 447, 447, 447]
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
    gameover = addtoCoordinate(d, 73, -55, 247, -60) #(d[0]+55, d[1]-72, d[0]+247, d[1]-60)
    g = addtoCoordinate(d, 73, -55, 84, -43) #(d[0]+55,d[1]-72,d[0]+67,d[1]-60) 
    e = addtoCoordinate(d, 144, -55, 155, -43) #(d[0]+127,d[1]-72,d[0]+139,d[1]-60)
    o = addtoCoordinate(d, 180, -55, 191, -43) #(d[0]+164,d[1]-72,d[0]+176,d[1]-60)
    r = addtoCoordinate(d, 252, -55, 264, -43) #(d[0]+235,d[1]-72,d[0]+247,d[1]-60)
    c1 = [60, 80, 85, 90, 90]
    c2 = [20, 20, 20, 20, 20]
    c3 = [100, 120, 125, 130, 130]
    c4 = [25, 25, 25, 25, 25]
class times():
    jumplen = [0.18, 0.18, 0.18, 0.17, 0.17]
    timepassed = [10.0, 20.0, 30.0, 40.0, 1000.0]

def restartGame():
    pyautogui.click(Coordinates.replayBtn)

def press(st,ind):
    pyautogui.keyDown(st)
    time.sleep(times.jumplen[ind])
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
    width, height = sh[0], sh[1]

    #if(a.sum()!=447):
    #    print(arr)
    flag = 1
    for x in arr:
        for y in x:
            if(y[0]==83 and y[1]==83 and y[2]==83 and flag==1):
                flag = 0
                break
                #print("Obstacle!!!")
                #global po
                #print(y,po)
                #po += 1
                
                
    #print(np.array(grayImage))
    #pp = input()
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
            #print(imageGrabGameOver(Coordinates.gameover),
            #    imageGrabGameOver(Coordinates.g),
            #    imageGrabGameOver(Coordinates.e),
            #    imageGrabGameOver(Coordinates.o),
            #    imageGrabGameOver(Coordinates.r))
            print(pyautogui.position())
        last=pyautogui.position()
    '''


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
        #a = time.time()
        res = imageGrab(ind)
        #b = time.time()
        #print(b-a)
        if(res == True):
            press('space', ind)
        elif(imageGrabRect(Coordinates.flyingdino)==True):
            press('down', ind)
main()