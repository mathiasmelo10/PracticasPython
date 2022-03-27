import imp
from re import search
import pyautogui, webbrowser
from time import sleep

def msgWpp():
    sleep(50)
    pyautogui.press("tab") 
    pyautogui.typewrite("just me") # Ingreso de nombre del contacto o grupo 
    pyautogui.press("enter") 
    for i in range(13):
        pyautogui.press("tab")
        continue
    pyautogui.typewrite("Buenas tardes!!. Recibistes un mensaje programado en Python de Mathi :) ")
    pyautogui.press("enter")


webbrowser.open('https://web.whatsapp.com')
msgWpp()