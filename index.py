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

        