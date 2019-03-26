import pyautogui
    
last = None
ccc = 0
while(True):
    if(last!=pyautogui.position()):
        print(pyautogui.position())
    last=pyautogui.position()
    #ccc += 1
    #if(ccc == 10):
    #    break
    #pyautogui.click(Coordinates.dinosaur)
    #pyautogui.click((Coordinates.g[2],Coordinates.g[3]))
    #pyautogui.click(Coordinates.replayBtn)
