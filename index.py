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
        rendeles = []
        while fut:
            print("---------APPLIKÁCIÓ---------")
            print("1: Étlap")
            print("2: Asztalfoglalás")
            print("3: Raktár")
            print("4: rendelés")
            print("5: Vásárlás")
            print("6: kilépés")
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
                print(self.vasarlas())
            elif valasztas == 6:
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
            self.asztalok[asztal - 1] = "szabad"
            Aplikacio.ment("asztalok.csv", self.asztalok)
    
#Megmutatja, hogy miből mennyi van a raktárban, és kiírja, ha valamiből kevés van és újra kell tölteni
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

#Itt le lehet adni a rendelést, az asztalhoz hozzárendeli a foglaló nevét és, hogy miket rendelt
    def rendeles(self):
        print("---------RENDELÉS---------")
        rendelesek = []
        rendele = True
        print("Melyik asztalhoz szeretnéd rendelni?")
        print("A következő asztalokhoz tudsz rendelni: ")
        for i in range(len(self.asztalok)):
            ideiglenes_valtozo = self.asztalok[i]
            ideiglenes_valtozo = ideiglenes_valtozo.split(";")
            if ideiglenes_valtozo[0] != "szabad":
                print(i+1,end=",")
        print('')
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
                cucc = self.menu[valasztas - 1].split(";")[0]
                self.hozzavalo_kereses(cucc)
                rendelesek.append(cucc)
        for i in range(len(self.asztalok)):
            if i == asztal - 1:
                sor = self.asztalok[i].split(";")
                nev = sor[0]
                self.asztalok[i] = nev + ";" + ";".join(rendelesek)
                Aplikacio.ment("asztalok.csv", self.asztalok)

    def hozzavalo_kereses(self, valasztas):
        leszedni = []
        ideiglenes = []
        for i in range(len(self.recept)):
            ideig= self.recept[i].split(";")
            if ideig[0] == valasztas:
                ideiglenes.append(ideig[1])
                ideiglenes.append(ideig[2])
                leszedni.append(ideiglenes)
                ideiglenes = []

        for z in range(len(leszedni)):
            for i in range(len(self.raktar)):
                ideges = self.raktar[i].split(";")
                if ideges[0] == leszedni[z][0]:
                    ideges[1] = int(ideges[1]) - int(leszedni[z][1])
                    ideges[1] = str(ideges[1])
                    self.raktar[i] = ";".join(ideges)
        Aplikacio.ment("raktar.csv", self.raktar)
    def vasarlas(self):
        print("---------VÁSÁRLÁS---------")
        ki = input("Ki volt a felszolgáló?")
        print("Melyik asztal szeretne vásárolni?")
        asztal = int(input("Válassz egy asztalt: "))
        ideiglenes = self.asztalok[asztal - 1].split(";")
        osszeg = 0
        for i in range(1,len(ideiglenes)):
            for z in range(len(self.menu)):
                if self.menu[z].split(";")[0] == ideiglenes[i]:
                    osszeg += int(self.menu[z].split(";")[1])
        vegso = [ki, ideiglenes[0], str(osszeg)]
        for i in range(1, len(ideiglenes)):
            vegso.append(ideiglenes[i])
        self.vasarlasok.append(";".join(vegso))
        self.asztalok[asztal - 1] = "szabad"
        Aplikacio.ment("vasarlasok.csv", self.vasarlasok)
        Aplikacio.ment("asztalok.csv", self.asztalok)



app = Aplikacio(raktar, menu, recept, vasarlasok, asztalok)
app.futás()
