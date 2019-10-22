import pyautogui
import time
import controls
import Coordinates
from db import Database
start = 0.0

def main():
    database = Database()
    
    
    moves = []

    while(True):
        global start
        start = time.clock()
        end = None
        controls.restartGame()

        if(len(moves)>1):
            database.insert(moves[:-1])

        while(True):
            timelen = time.clock() - start
            for i,t in enumerate(Coordinates.times.timepassed):
                if(timelen<t):
                    ind = i
                    break
    
            if(controls.gameEnded()):
                break
                
            #print(a-b)
            #a = time.time()
            res = controls.imageGrab(start)
            #b = time.time()
            #print(b-a)

            if(type(res) is tuple):
                res, firstPixel = res

                end = time.clock()
                moves.append((round(end - start, 2), firstPixel))

            if(res == 1):
                controls.press('space', ind)
            elif(res == 2):
                controls.press('down', ind)
        pyautogui.click((1000, 500))
            
        end = time.clock()
        print(end - start, ind)
        time.sleep(3.0)
        controls.saveScreenShot()
        controls.restartGame()
        start = time.clock()
            
main()