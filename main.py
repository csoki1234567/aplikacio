import menukiiras
import funkciok

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
        """Inicializálja az applikációt a fájlok tartalmával.
        Args:
            raktar (list): A raktár tartalma.
            menu (list): Az étlap tartalma.
            recept (list): A receptek tartalma.
            vasarlasok (list): A vásárlások tartalma.
            asztalok (list): Az asztalok tartalma.
        """
        self.raktar = raktar
        self.menu = menu
        self.recept = recept
        self.vasarlasok = vasarlasok
        self.asztalok = asztalok

#Az applikáció menüje
    def futás(self):
        fut = True
        rendeles = []
        while fut:
            menukiiras.fomenukiir()
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
                print(self.menuhozazdas())
            elif valasztas == 7:
                fut = False
            else:
                print("Érvénytelen választás.")

#Megnyitja az étlapot, és megmutatja mi mennyibe kerül

    def menumutatas(self):
        funkciok.etlapmutat(self.menu)

#Megmutatja az asztalokat, és lehetőséget ad a foglalásra vagy a foglalás törlésére
    def asztalfoglalás(self):
        funkciok.asztalfoglalas(self.asztalok)

#Megmutatja, hogy miből mennyi van a raktárban, és kiírja, ha valamiből kevés van és újra kell tölteni
    def raktarmutatas(self):
        funkciok.raktars(self.raktar)
#Itt le lehet adni a rendelést, az asztalhoz hozzárendeli a foglaló nevét és, hogy miket rendelt
    def rendeles(self):
        funkciok.rendeles(self.asztalok,self.menu)
#Itt lehet lezárni a rendelést, megmutatja a végösszeget, és kiírja, hogy ki volt a felszolgáló
    def vasarlas(self):
        funkciok.vasarlas(self.vasarlasok, self.asztalok, self.menu)
#Itt lehet hozzáadni új ételt a menühöz
    def menuhozazdas(self):
        funkciok.etlaphozzadas(self.menu)

app = Aplikacio(raktar, menu, recept, vasarlasok, asztalok)
app.futás()
