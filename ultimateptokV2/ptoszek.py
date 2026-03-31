import pyautogui
import webbrowser
import os
import time
import ctypes
path = "index.html"
for i in range(10):

   webbrowser.open_new_tab(path)
    # Czekamy aż się załaduje (na szkolnym kompie dajemy 4 sekundy)

    # KLIKNIĘCIE I AKTYWACJA
   width, height = pyautogui.size()
     



     
   pyautogui.click(width / 2, height / 2)  # Klika w środek
   pyautogui.click(width / 2, height / 2)  # Klika w środek
   pyautogui.click(width / 2, height / 2)  # Klika w środek
   pyautogui.click(width / 2, height / 2)  # Klika w środek
   pyautogui.click(width / 2, height / 2)  # Klika w środek

   pyautogui.press('enter')
   pyautogui.press('f11')  
   pyautogui.press('space')  
   pyautogui.press('enter')
   pyautogui.press('enter')
   pyautogui.press('enter')
   pyautogui.press('enter')
    
