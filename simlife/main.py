import json

class Game:
    def __init__(self, name, surname, year):
        self.name = name
        self.surname = surname
        self.year = year
    def save(self, save):
        data = json.dumps(save)
        with open("dane.json", "w") as file:
            file.write(data)
    def main(self):
        print("ok")

def start():
    print("*************************")
    print("Witaj w SimLife!")
    print("1.Nowa Gra")
    print("2.Kontynuuj")
    print("3.Wyjdź")
    print("*************************")
    start = input()

    if start == "1":
        name = input("Jak ma na imię twój sim?\n")
        surname = input("Jak ma na nazwisko twój sim?\n")
        year = input("W którym roku urodził się twój sim?\n")
        player = Game(name, surname, year)
        save = {"name": name, "surname": surname, "year": year}

        player.save(save)
        player.main()

    elif start == "2":
        with open("dane.json", "r") as file:
            data = file.read()

        if data == "":
            print("Nie można kontynuować")
            quit()
        try:
            data = json.loads(data)
            name, surname, year = data["name"], data["surname"], data["year"]
        except:
            print("Coś poszło nie tak")
            quit()
        
        player = Game(name, surname, year)
        player.main()

    elif start == "3":
        quit()

start()