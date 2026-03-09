def betoltes(fajl):
    with open(fajl, "r", encoding="utf-8") as f:
        tartalom = f.readlines()
        tartalom = [x.strip() for x in tartalom]
    return tartalom

raktar = betoltes("raktar.csv")
menu = betoltes("menu.csv")
recept = betoltes("recept.csv")
vasarlasok = betoltes("vasarlasok.csv")
