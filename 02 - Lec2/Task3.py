
'''
Tsak3
1 - Run vscode
2 - Search for extention
3 - install extention
'''

import pyautogui
import time
import os

pyautogui.hotkey('win')                 # Press win button.
time.sleep(2)                           # Wait for 2 seconds.
searchKey ='vscode'                     

for i in range(0,6):                    # Search for 'vscode' with delay 0.25 second to simulate human. 
    pyautogui.write(searchKey[i])               
    time.sleep(0.25)

pyautogui.hotkey('enter')
time.sleep(5)


mypath = os.path.dirname(os.path.realpath(__file__))+"/Ex.png"          # Get the current directory path.

isFound = None

while isFound == None :                                                 # Make sure the photo 'Extention icon' is found.
    isFound = pyautogui.locateOnScreen(mypath,confidence=0.7)


pyautogui.moveTo(isFound[0]+5,isFound[1]+200,duration=0.5)              # Move the mouse to the icon.
time.sleep(3)                                                           # Wait 3 seconds
pyautogui.click()                                                       # ->> Click <<-

##########################################################
'''
searchKey ='clangd'

for i in range(0,6):   
    pyautogui.write(searchKey[i])               
    time.sleep(0.25)

mypath = os.path.dirname(os.path.realpath(__file__))+"/clangd.png"

isFound = None
time.sleep(4)

while isFound == None :
    isFound = pyautogui.locateOnScreen(mypath,confidence=0.7)


pyautogui.moveTo(isFound[0]+210,isFound[1]+60,duration=0.5)
time.sleep(3)
#pyautogui.click()

# Select all text in the search box (Ctrl+A)
pyautogui.hotkey('ctrl', 'a')
time.sleep(0.5)
pyautogui.press('delete')
'''
##########################################################
searchKey ='c++ testmate'

for i in searchKey:   
    pyautogui.write(i)               
    time.sleep(0.25)

mypath = os.path.dirname(os.path.realpath(__file__))+"/testmate.png"
isFound = None
time.sleep(4)
while isFound == None :
    isFound = pyautogui.locateOnScreen(mypath,confidence=0.7)

pyautogui.moveTo(isFound[0]+210,isFound[1]+60,duration=0.5)
time.sleep(3)
#pyautogui.click()

# Select all text in the search box (Ctrl+A)
mypath = os.path.dirname(os.path.realpath(__file__))+"/search.png"
isFound = None
time.sleep(4)
while isFound == None :
    isFound = pyautogui.locateOnScreen(mypath,confidence=0.7)

pyautogui.moveTo(isFound[0]+10,isFound[1]+10,duration=0.5)
time.sleep(3)
pyautogui.click()
pyautogui.keyDown('backspace')
time.sleep(10)
pyautogui.keyUp('backspace')

##########################################################
'''
searchKey ='c++ helper'

for i in searchKey:   
    pyautogui.write(i)               
    time.sleep(0.25)

mypath = os.path.dirname(os.path.realpath(__file__))+"/helper.png"

isFound = None
time.sleep(4)

while isFound == None :
    isFound = pyautogui.locateOnScreen(mypath,confidence=0.7)


pyautogui.moveTo(isFound[0]+210,isFound[1]+56,duration=0.5)
time.sleep(3)
#pyautogui.click()

# Select all text in the search box (Ctrl+A)
pyautogui.hotkey('ctrl', 'a')
time.sleep(0.5)
pyautogui.press('delete')
'''
