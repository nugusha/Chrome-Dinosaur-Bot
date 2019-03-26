import pyautogui
import time
import controls
import Coordinates
start = 0.0

def main():
    a=0
    b=0
    global start
    start = time.clock()
    end = None
    controls.restartGame()
    while(True):    
        timelen = time.clock() - start
        for i,t in enumerate(Coordinates.times.timepassed):
            if(timelen<t):
                ind = i
                break
 
        if(controls.gameEnded()==True):
            pyautogui.click((1000,500))
            
            end = time.clock()
            print(end - start, ind)
            time.sleep(3.0)
            controls.saveScreenShot()
            controls.restartGame()
            start = time.clock()
            continue
            
        #print(a-b)
        #a = time.time()
        res = controls.imageGrab(ind, True, start)
        #b = time.time()
        #print(b-a)
        if(res == 1):
            controls.press('space', ind)
        elif(res == 2):
            controls.press('down', ind)
main()