import pyautogui
import time
import controls
import Coordinates
import random
from db import Database
start = 0.0

def main():
    database = Database()
    
    while(True):
        
        moves = []
        coef1 = random.uniform(0.5, 2.0) # 1.75
        coef2 = random.randint(40, 120)

        while(30.0*coef1 + coef1 > 150):
            coef1 = random.uniform(0.5, 2.0) # 1.75
            coef2 = random.randint(40, 120)
        
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
    
            if(controls.gameEnded()):
                break
            
            res = controls.imageGrab(start, coef1, coef2)

            if(type(res) is tuple):
                res, firstPixel = res

                end = time.clock()
                moves.append((round(end - start, 2), firstPixel,1))

            if(res == 1):
                controls.press('space', ind)
            elif(res == 2):
                controls.press('down', ind)
            

        if(len(moves)>0):
            if(len(moves)>1):
                a,b,c = moves[-2]
                moves[-2] = (a,b,2)
            a,b,c = moves[-1]
            moves[-1] = (a,b,0)
            database.insert(moves)
            print("Add in Database!!!")

        end = time.clock()
        database.insertResult(coef1,coef2,end-start)
        print(end - start, ind)
        time.sleep(3.0)
        controls.saveScreenShot()
        controls.restartGame()
        start = time.clock()

if __name__ == "__main__":
    main()