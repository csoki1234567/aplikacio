def betoltes(fajl):
    with open(fajl, "r", encoding="utf-8") as f:
        tartalom = f.readlines()
        tartalom = [x.strip() for x in tartalom]
    return tartalom

raktar = betoltes("raktar.csv")
menu = betoltes("menu.csv")
recept = betoltes("recept.csv")
vasarlasok = betoltes("vasarlasok.csv")
class Aplikacio:
    def __init__(self, raktar, menu, recept, vasarlasok):
        self.raktar = raktar
        self.menu = menu
        self.recept = recept
        self.vasarlasok = vasarlasok
    def ment(fajl, sorok):
        with open(fajl, "w", encoding="utf-8") as f:
            f.write("\n".join(sorok) + ("\n" if sorok else ""))
    def futás(self):
        fut = True
        while fut:
            print("---------APPLIKÁCIÓ---------")
            print("1: Étlap megmutatása")
            print("2: Kilépés")
            print("----------------------------")
            valasztas = int(input("Válassz egy lehetőséget: "))
            if valasztas == 1:
                print(self.menumutatas())
            elif valasztas == 2:
                fut = False
            else:
                print("Érvénytelen választás.")
    def menumutatas(self):
        print("---------ÉTLAP---------")
        i = 1
        for item in self.menu:
            item = item.split(";")
            print(f"{i}: {item[0]} - {item[1]} Ft")
            i += 1
        print("-----------------------")


app = Aplikacio(raktar, menu, recept, vasarlasok)
app.futás()

