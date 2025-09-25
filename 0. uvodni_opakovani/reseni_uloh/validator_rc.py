import datetime


def ziskej_rok_narozeni(rok):
    rok = int(rok)
    if int(rok) <= 25 % 100:
        return 2000 + rok
    else:
        return 1900 + rok
    

def validuj_rc(rc):
    if len(rc) != 11:
        print("Délka není validní")
        return False

    if rc[6] != "/":
        print("Chybí znak /")
        return False

    rok = rc[0:2]
    mesic = rc[2:4]
    den = rc[4:6]
    kontrol = rc[7:11]

    if not (rok.isdigit() or mesic.isdigit() or den.isdigit() or kontrol.isdigit()):
        print("Znaky RČ nejsou validní")
        return False

    #rok
    rok = ziskej_rok_narozeni(rok)

    # pohlavi
    mesic = int(mesic)
    if mesic > 50:
        pohlavi = "Žena"
        mesic -= 50
    else:
        pohlavi = "Muž"

    if not (1 <= mesic <= 12):
        print("Měsíc není korektní")
        return False
    
    # den
    den = int(den)
    if not (1 <= den <= 31):
        print("Den není korektní")
        return False

    # vystup
    print(f"Den narození: {den}.{mesic}.{rok}")
    print("Pohlaví:", pohlavi)

    return True


if validuj_rc("850126/1158"):
    print("Validní rodné číslo")