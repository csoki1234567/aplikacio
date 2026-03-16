#Betölti a fájlokat a programba
def betoltes(fajl):
    with open(fajl, "r", encoding="utf-8") as f:
        tartalom = f.readlines()
        tartalom = [x.strip() for x in tartalom]
    return tartalom

raktar = betoltes("raktar.csv")
menu = betoltes("menu.csv")
recept = betoltes("recept.csv")
vasarlasok = betoltes("vasarlasok.csv")
asztalok = betoltes("asztalok.csv")

#Applikáció
class Aplikacio:

#Lementi a fájlokat a classbe
    def __init__(self, raktar, menu, recept, vasarlasok, asztalok):
        self.raktar = raktar
        self.menu = menu
        self.recept = recept
        self.vasarlasok = vasarlasok
        self.asztalok = asztalok

#Menti a fájlokat a programba
    def ment(fajl, sorok):
        with open(fajl, "w", encoding="utf-8") as f:
            f.write("\n".join(sorok) + ("\n" if sorok else ""))

#Az applikáció menüje
    def futás(self):
        fut = True
        while fut:
            print("---------APPLIKÁCIÓ---------")
            print("1: Étlap")
            print("2: Asztalfoglalás")
            print("3: Raktár")
            print("4: rendelés")
            print("5: kilépés")
            print("----------------------------")
            valasztas = int(input("Válassz egy lehetőséget: "))
            if valasztas == 1:
                print(self.menumutatas())
            elif valasztas == 2:
                print(self.asztalfoglalás())
            elif valasztas == 3:
                print(self.raktarmutatas())
            elif valasztas == 4:
                print(self.rendeles())
            elif valasztas == 5:
                fut = False
            else:
                print("Érvénytelen választás.")

#Megnyitja az étlapot, és megmutatja mi mennyibe kerül
    def menumutatas(self):
        print("---------ÉTLAP---------")
        i = 1
        for item in self.menu:
            item = item.split(";")
            print(f"{i}: {item[0]} - {item[1]} Ft")
            i += 1
        print("-----------------------")
#Megmutatja az asztalokat, és lehetőséget ad a foglalásra vagy a foglalás törlésére
    def asztalfoglalás(self):
        print("---------Asztalok---------")
        y = 1
        for i in self.asztalok:
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
            self.asztalok[asztal - 1] = kit
            Aplikacio.ment("asztalok.csv", self.asztalok)
        elif valasztas == 2:
            print("-----------------------")
            asztal = int(input("Melyik asztal foglalását szeretnéd törölni? "))
            self.asztalok[asztal - 1] = "Szabad"
            Aplikacio.ment("asztalok.csv", self.asztalok)
    
    def raktarmutatas(self):
        print("---------RAKTÁR---------")
        t = []
        i = 1
        for item in self.raktar:
            item = item.split(";")
            print(f"{i}: {item[0]} - {item[1]}{item[2]}")
            if int(item[1]) < 200:
                t.append(item[0])
            i += 1
        print("\n", "A hozzávalók amiket fel kell tölteni: ")
        for kaja in t:
            print(kaja)
    def rendeles(self):
        print("---------RENDELÉS---------")
        rendelesek = []
        rendele = True
        print("melyik asztalhoz szeretnéd rendelni?")
        asztal = int(input("Válassz egy asztalt: "))
        while rendele:
            print("Mit szeretnél rendelni? (0-val kiléphetsz)")
            i = 1
            for item in self.menu:
                item = item.split(";")
                print(f"{i}: {item[0]} - {item[1]} Ft")
                i += 1
            valasztas = int(input("Válassz egy lehetőséget: "))
            if valasztas == 0:
                rendele = False
                print("Rendelés vége.")
            else:
                rendelesek.append(self.menu[valasztas - 1])
        return rendelesek,asztal
            


app = Aplikacio(raktar, menu, recept, vasarlasok, asztalok)
app.futás()
