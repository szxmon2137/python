import time
import os
from colorama import Fore

def winChecker(plansza):
    #0 - gra trwa, 1 - wygrana kółek, 2 - wygrana krzyżyków, 3 - remis

    #OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
    #wygrana poziomo
    for i in range(1, 4):
        if plansza[i][1] == "O" and plansza[i][2] == "O" and plansza[i][3] == "O":
            return 1

    # wygrana pionowo
    for i in range(1, 4):
        if plansza[1][i] == "O" and plansza[2][i] == "O" and plansza[3][i] == "O":
            return 1

    # wygrana na ukos
    if plansza[1][1] == "O" and plansza[2][2] == "O" and plansza[3][3] == "O":
        return 1

    if plansza[1][3] == "O" and plansza[2][2] == "O" and plansza[3][1] == "O":
        return 1


    #XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    #wygrana poziomo
    for i in range(1, 4):
        if plansza[i][1] == "X" and plansza[i][2] == "X" and plansza[i][3] == "X":
            return 2

    # wygrana pionowo
    for i in range(1, 4):
        if plansza[1][i] == "X" and plansza[2][i] == "X" and plansza[3][i] == "X":
            return 2

    # wygrana na ukos
    if plansza[1][1] == "X" and plansza[2][2] == "X" and plansza[3][3] == "X":
        return 2

    if plansza[1][3] == "X" and plansza[2][2] == "X" and plansza[3][1] == "X":
        return 2


    # remis
    remis = 0
    for row in range(1, 4):
        for column in range(1, 4):
            if plansza[row][column] != " ":
                remis += 1
    if remis == 9:
        return 3

    return 0

#drukarka
def mapPrinter(plansza):
    print(Fore.GREEN + "<--------->")
    print(f" {plansza[1][1]} | {plansza[1][2]} | {plansza[1][3]} ")
    print(f" {plansza[2][1]} | {plansza[2][2]} | {plansza[2][3]} ")
    print(f" {plansza[3][1]} | {plansza[3][2]} | {plansza[3][3]} ")
    print("<--------->" + Fore.RESET)

#główna funkcja
def lokalna():
    plansza = {1: {1: " ", 2: " ", 3: " "},
               2: {1: " ", 2: " ", 3: " "},
               3: {1: " ", 2: " ", 3: " "}}
    tura = 1
    os.system("cls")
    time.sleep(0.5)
    mapPrinter(plansza)

    while winChecker(plansza) == 0:
        print(f"Tura {tura}")
        

        #Kolej kółek
        time.sleep(0.5)
        print(Fore.BLUE + "Gracz 1 (O)" + Fore.RESET)
        time.sleep(0.5)

        while True:
            row = input("Podaj rząd(poziomo)(1-3): ").strip()
            column = input("Podaj kolumne(pionowo)(1-3): ").strip()

            if row.isnumeric() and column.isnumeric():
                row = int(row)
                column = int(column)
            else:
                print("Zła odpowiedź")
                continue
            os.system("cls")
            # Sprawdzenie czy odpowiedź jest dobra
            if row in range(1, 4):
                if column in range(1, 4):

                    # Sprawdzenie czy pole jest zajęte
                    if plansza[row][column] != " ":
                        print("To pole jest już zajęte")

                    else:
                        plansza[row][column] = "O"
                        mapPrinter(plansza)
                        break
                else:
                    print("Zła odpowiedź")
            else:
                print("Zła odpowiedź")

        #Sprawdzenie stanu gry
        if winChecker(plansza) == 3:
            print(Fore.YELLOW + "Remis!" + Fore.RESET)
            time.sleep(1)
            break
        elif winChecker(plansza) == 2:
            print(Fore.RED + "Wygrana Krzyżyków!" + Fore.RESET)
            time.sleep(1)
            break
        elif winChecker(plansza) == 1:
            print(Fore.BLUE + "Wygrana Kółek!" + Fore.RESET)
            time.sleep(1)
            break

        #Kolej krzyżyków
        time.sleep(0.5)
        print(Fore.RED + "Gracz 2 (X)" + Fore.RESET)
        time.sleep(0.5)

        while True:
            row = input("Podaj rząd(poziomo)(1-3): ").strip()
            column = input("Podaj kolumne(pionowo)(1-3): ").strip()

            if row.isnumeric() and column.isnumeric():
                row = int(row)
                column = int(column)
            else:
                print("Zła odpowiedź")
                continue
            os.system("cls")
            #Sprawdzenie czy odpowiedź jest dobra
            if row in range(1, 4):
                if column in range(1, 4):
                    # Sprawdzenie czy pole jest zajęte
                    if plansza[row][column] != " ":
                        print("To pole jest już zajęte")
                    else:
                        plansza[row][column] = "X"
                        mapPrinter(plansza)
                        tura += 1
                        break
                else:
                    print("Zła odpowiedź")
            else:
                print("Zła odpowiedź")

        #Sprawdzenie stanu gry
        if winChecker(plansza) == 3:
            print(Fore.YELLOW + "Remis!" + Fore.RESET)
            time.sleep(1)
            break
        elif winChecker(plansza) == 2:
            print(Fore.RED + "Wygrana Krzyżyków!" + Fore.RESET)
            time.sleep(1)
            break
        elif winChecker(plansza) == 1:
            print(Fore.BLUE + "Wygrana Kółek!" + Fore.RESET)
            time.sleep(1)
            break

os.system("cls")
print(Fore.CYAN + "Kółko i Krzyżyk 1.1" + Fore.RESET) #22:36 16.01.2026

while True:
    time.sleep(0.5)
    print("1. Lokalna")
    time.sleep(0.5)
    print(Fore.GREEN + "2. Z botem (Coming Soon...)" + Fore.RESET)
    time.sleep(0.5)
    print(Fore.RED + "3. Wyjdź" + Fore.RESET)
    time.sleep(0.5)
    user = input(Fore.YELLOW + "Tryb gry: " + Fore.RESET).strip()

    if user.isnumeric():
        user = int(user)
    else:
        print("Zła odpowiedź")
        continue

    if user == 1:
        lokalna()
    elif user == 2:
        print("Coming Soon...")
        continue
    elif user == 3:
        quit()
    else:
        print("Zła odpowiedź")