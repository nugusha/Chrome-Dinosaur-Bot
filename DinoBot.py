from PIL import ImageGrab, ImageOps
import pyautogui
import time
import numpy as np
from numpy import *
class consts():
    obstacles = [397,547,697]
    gameoverCNT = 2634
    gameoverCNTLet = 474
    flyingdino = 500
    
class Coordinates():
    replayBtn = (340, 416)
    dinosaur = (190, 441)
    flyingdino = (290,413,298,426)
    gameover = (245, 369, 437, 381)
    g = (245,369,257,381)
    e = (317,369,329,381)
    o = (354,369,366,381)
    r = (425,369,437,381)
    c1 = [60, 60, 60]
    c2 = [0, 0, 0]
    c3 = [90, 120, 150]
    c4 = [5, 5, 5]
class times():
    jumplen = [0.17, 0.16, 0.10]

def restartGame():
    pyautogui.click(Coordinates.replayBtn)

def pressSpace(ind):
    pyautogui.keyDown('space')
    time.sleep(times.jumplen[ind])
    pyautogui.keyUp('space')
    
def imageGrab(ind):
    X = Coordinates.dinosaur[0]
    Y = Coordinates.dinosaur[1]
    cc1 = Coordinates.c1[ind]
    cc2 = Coordinates.c2[ind]
    cc3 = Coordinates.c3[ind]
    cc4 = Coordinates.c4[ind]
    box = (X+cc1, Y+cc2, 
           X+cc3, Y+cc4)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    return a.sum()

def imageGrabGameOver(rect):
    box = (rect)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    return a.sum()
    
def main():
    '''
    last = None
    while(True):
        if(last!=pyautogui.position()):
            print(imageGrabGameOver(Coordinates.gameover),
                imageGrabGameOver(Coordinates.g),
                imageGrabGameOver(Coordinates.e),
                imageGrabGameOver(Coordinates.o),
                imageGrabGameOver(Coordinates.r))
            print(pyautogui.position())
        last=pyautogui.position()
    '''


    start = time.clock()
    end = None
    cnt = 0
    restartGame()
    while(True):    
        timelen = time.clock() - start
        if(timelen<10.0):
            ind = 0
        elif(timelen<40.0):
            ind = 1
        elif(timelen<1000.0):
            ind = 2
            
        if(#imageGrabGameOver(Coordinates.gameover)==consts.gameoverCNT or
            imageGrabGameOver(Coordinates.g)==consts.gameoverCNTLet or
            imageGrabGameOver(Coordinates.e)==consts.gameoverCNTLet):
            #imageGrabGameOver(Coordinates.o)==consts.gameoverCNTLet or
            #imageGrabGameOver(Coordinates.r)==consts.gameoverCNTLet
            
            end = time.clock()    
            print(end - start, ind)
            time.sleep(3.0)
            pic = pyautogui.screenshot()
            r = random.randint(100000, 999999)
            pic.save('screenshot'+str(r)+'.png')
            cnt += 1
            if(cnt == 10):
                break
            restartGame()
            start = time.clock()
            continue

        if(imageGrab(ind) != consts.obstacles[ind]):
            pressSpace(ind)
main()