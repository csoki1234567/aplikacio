
def etlapmutat(menu):
    """Megnyitja az étlapot, és megmutatja mi mennyibe kerül.
    Args:
        menu (list): Az étlap tartalma.
    """
    print("---------ÉTLAP---------")
    i = 1
    for item in menu:
        item = item.split(";")
        print(f"{i}: {item[0]} - {item[1]} Ft")
        i += 1
    print("-----------------------")

def asztalfoglalas(asztalok):
    """Megmutatja az asztalokat, és lehetőséget ad a foglalásra vagy a foglalás törlésére.
    Args:
        asztalok (list): Az asztalok tartalma.
    """
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
        ment("asztalok.csv", asztalok)
    elif valasztas == 2:
        print("-----------------------")
        asztal = int(input("Melyik asztal foglalását szeretnéd törölni? "))
        asztalok[asztal - 1] = "szabad"
        ment("asztalok.csv", asztalok)

def rendeles(asztalok,menu):
    """Megmutatja az asztalokat, és lehetőséget ad a rendelésre.
    Args:
        asztalok (list): Az asztalok tartalma.
        menu (list): Az étlap tartalma.
    """
    print("---------RENDELÉS---------")
    rendelesek = []
    rendele = True
    print("Melyik asztalhoz szeretnéd rendelni?")
    print("A következő asztalokhoz tudsz rendelni: ")
    for i in range(len(asztalok)):
        ideiglenes_valtozo = asztalok[i]
        ideiglenes_valtozo = ideiglenes_valtozo.split(";")
        if ideiglenes_valtozo[0] != "szabad":
            print(i+1,end=",")
    print('')
    asztal = int(input("Válassz egy asztalt: "))
    while rendele:
        print("Mit szeretnél rendelni? (0-val kiléphetsz)")
        i = 1
        for item in menu:
            item = item.split(";")
            print(f"{i}: {item[0]} - {item[1]} Ft")
            i += 1
        valasztas = int(input("Válassz egy lehetőséget: "))
        if valasztas == 0:
            rendele = False
            print("Rendelés vége.")
        else:
            cucc = menu[valasztas - 1].split(";")[0]
            hozzavalo_kereses(cucc)
            rendelesek.append(cucc)
    for i in range(len(asztalok)):
        if i == asztal - 1:
            sor = asztalok[i].split(";")
            nev = sor[0]
            asztalok[i] = nev + ";" + ";".join(rendelesek)
            ment("asztalok.csv", asztalok)

def hozzavalo_kereses(valasztas):
    """Megkeresi a hozzávalókat, és leveszi a raktárból.
    Args:
        valasztas (str): A választott étel neve.
    """
    leszedni = []
    ideiglenes = []
    for i in range(len(recept)):
        ideig= recept[i].split(";")
        if ideig[0] == valasztas:
            ideiglenes.append(ideig[1])
            ideiglenes.append(ideig[2])
            leszedni.append(ideiglenes)
            ideiglenes = []
    for z in range(len(leszedni)):
        for i in range(len(raktar)):
            ideges = raktar[i].split(";")
            if ideges[0] == leszedni[z][0]:
                ideges[1] = int(ideges[1]) - int(leszedni[z][1])
                ideges[1] = str(ideges[1])
                raktar[i] = ";".join(ideges)
    ment("raktar.csv", raktar)


def vasarlas(vasarlasok, asztalok, menu): 
    """Megmutatja a vásárlásokat, és lehetőséget ad a vásárlásra.
    Args:        
        vasarlasok (list): A vásárlások tartalma.
        asztalok (list): Az asztalok tartalma.
        menu (list): Az étlap tartalma.
    """   
    print("---------VÁSÁRLÁS---------")
    ki = input("Ki volt a felszolgáló?")
    print("Melyik asztal szeretne vásárolni?")
    asztal = int(input("Válassz egy asztalt: "))
    ideiglenes = asztalok[asztal - 1].split(";")
    osszeg = 0
    for i in range(1,len(ideiglenes)):
        for z in range(len(menu)):
            if menu[z].split(";")[0] == ideiglenes[i]:
                osszeg += int(menu[z].split(";")[1])
    vegso = [ki, ideiglenes[0], str(osszeg)]
    for i in range(1, len(ideiglenes)):
        vegso.append(ideiglenes[i])
    vasarlasok.append(";".join(vegso))
    asztalok[asztal - 1] = "szabad"
    ment("vasarlasok.csv", vasarlasok)
    ment("asztalok.csv", asztalok)

def etlaphozzadas(menu):
    """Lehetőséget ad az étlaphoz új étel hozzáadására.
    Args:
        menu (list): Az étlap tartalma.
    """
    print("---------ÉTLAPHOZZÁADÁS---------")
    nev = input("Mi legyen az étel neve? ")
    ar = input("Mennyibe kerüljön? ")
    uj = nev + ";" + ar
    menu.append(uj)
    ment("menu.csv", menu)
    hozzavalo = input("Milyen hozzávalókból áll? (formátum: hozzávaló;mennyiség, több hozzávaló esetén vesszővel elválasztva) ")
    hozzavalo = hozzavalo.split(",")
    for i in range(len(hozzavalo)):
        sor = nev + ";" + hozzavalo[i]
        recept.append(sor)
    ment("recept.csv", recept)

def ment(fajl, sorok):
        with open(fajl, "w", encoding="utf-8") as f:
            f.write("\n".join(sorok) + ("\n" if sorok else ""))

def betoltes(fajl):
    with open(fajl, "r", encoding="utf-8") as f:
        tartalom = f.readlines()
        tartalom = [x.strip() for x in tartalom]
    return tartalom

recept = betoltes("recept.csv")
raktar = betoltes("raktar.csv")


