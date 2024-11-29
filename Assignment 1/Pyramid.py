import pyautogui
import time
levels = int(input())
time.sleep(0.5)
pyautogui.typewrite(str(levels))  
pyautogui.press('enter')          
for i in range(1, levels + 1):
    pyautogui.typewrite('#' * i) 
    pyautogui.press('enter')      
