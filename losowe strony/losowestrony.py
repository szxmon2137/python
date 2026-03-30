import webbrowser
import random
import time
from tranco import Tranco
tranco = Tranco()
lista = tranco.list().top(1000000)
while True:
    try:
        ilosc = int(input("Ile stron otwierać?\n"))
        break
    except ValueError:
        print("Zła wartość")
        

url = "https://"
while True:
    
    for i in range(ilosc):
        rand = random.randint(0, 999999)
        webbrowser.open_new_tab(url + lista[rand])
        time.sleep(random.uniform(0.1, 0.4))
    x = input("Dalej? t/n\n")
    if x.lower().strip() == "n":
        break