import imp
from re import search
import pyautogui, webbrowser
from time import sleep

webbrowser.open('https://web.whatsapp.com/')

sleep(30)

pyautogui.press("tab") 
pyautogui.typewrite("just me")
pyautogui.press("enter") 
for i in range(12):
    pyautogui.press("tab")
    continue
pyautogui.typewrite("Mensaje programado")
pyautogui.press("enter")