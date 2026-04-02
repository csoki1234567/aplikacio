def fomenukiir():
    print("---------APPLIKÁCIÓ---------")
    print("1: Étlap")
    print("2: Asztalfoglalás")
    print("3: Raktár")
    print("4: rendelés")
    print("5: Vásárlás")
    print("6: Étlap hozzáadása")
    print("7: kilépés")
    print("----------------------------")

def raktars(raktar):
    print("---------RAKTÁR---------")
    t = []
    i = 1
    for item in raktar:
        item = item.split(";")
        print(f"{i}: {item[0]} - {item[1]}{item[2]}")
        if int(item[1]) < 200:
            t.append(item[0])
        i += 1
    print("\n", "A hozzávalók amiket fel kell tölteni: ")
    for kaja in t:
        print(kaja)
