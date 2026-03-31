import pyautogui
import webbrowser
import time

class Ptok:
   def __init__(self, quantity: int, path: str):
      self.quantity = quantity
      self.path = path

   def main(self):
      for i in range(self.quantity):
         webbrowser.open_new_tab(self.path)

         time.sleep(0.1)
         self.click()
         
   def click(self):
      width, height = pyautogui.size()
      for i in range(5):
         pyautogui.click(width / 2, height / 2)
         time.sleep(0.1)
      for i in range(5):
         pyautogui.press('enter')
         pyautogui.press('f11')  
         pyautogui.press('space')
         time.sleep(0.1)

ptosz = Ptok(10, "https://ptoszek.pl")
ptosz.main()
      
