import imp
from re import search
import pyautogui, webbrowser
from time import sleep

def msgWpp():
    sleep(50)
    pyautogui.press("tab") 
    pyautogui.typewrite("mas que una familia vmkg")
    pyautogui.press("enter") 
    for i in range(13):
        pyautogui.press("tab")
        continue
    pyautogui.typewrite("Buenas tardes!!. Que vamos a comer hoy?. Red Market cierra a las 21:00 y el Super de Roberto a las 21:30!")
    pyautogui.press("enter")


webbrowser.open('https://web.whatsapp.com')
msgWpp()