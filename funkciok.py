import index

def etlapmutat(menu):
    print("---------ÉTLAP---------")
    i = 1
    for item in menu:
        item = item.split(";")
        print(f"{i}: {item[0]} - {item[1]} Ft")
        i += 1
    print("-----------------------")

def asztalfoglalas(asztalok):
    print("---------Asztalok---------")
    y = 1
    for i in asztalok:
        print(f"{y}: {i}")
        y += 1
    print("-----------------------")
    print("mit akarsz csinálni: ")
    print("-----------------------")
    print("1: Asztalfoglalás")
    print("2: Asztalfoglalás törlése")
    print("-----------------------")
    valasztas = int(input("Válassz egy lehetőséget: \n"))
    if valasztas == 1:
        print("-----------------------")
        asztal = int(input("Melyik asztalra szeretnél foglalni? "))
        kit = input("Kinek a nevére szeretnél foglalni? ")
        asztalok[asztal - 1] = kit
        index.Aplikacio.ment("asztalok.csv", asztalok)
    elif valasztas == 2:
        print("-----------------------")
        asztal = int(input("Melyik asztal foglalását szeretnéd törölni? "))
        asztalok[asztal - 1] = "szabad"
        index.Aplikacio.ment("asztalok.csv", asztalok)

