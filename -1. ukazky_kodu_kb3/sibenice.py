import random


def generuj_slovo():
  slova = ["cheese", "dog", "get", "chair", "tank", "tea", "light", "pineapple"]
  return random.choice(slova)


def vypis_zivoty(zivoty):
  print("Máš právě", zivoty, "životů")


def inicializace():
  hadane_slovo = generuj_slovo()
  zivoty = 7
  print("Zahrajem si šibenici")
  vypis_zivoty(zivoty)
  hadane_znaky = []
  return hadane_slovo, zivoty, hadane_znaky


def ukaz_hadane(hadane_slovo, hadane_znaky):
  print("Hádané slovo: ", end="")
  for znak in hadane_slovo:
    if znak in hadane_znaky:
      print(znak + " ", end="")
    else:
      print("_ ", end="")


def cyklus_hry(hadane_slovo, zivoty, hadane_znaky):
  pismeno = input("Zadej písmeno k hádání: ")[0].lower()

  if pismeno in hadane_slovo:
    hadane_znaky.append(pismeno)
    ukaz_hadane(hadane_slovo, hadane_znaky)
  else:
    print("Neuhodl jsi.")
    zivoty -= 1
  vypis_zivoty(zivoty)
  print()
  return hadane_slovo, zivoty, hadane_znaky


def sibenice():
  hadane_slovo, zivoty, hadane_znaky = inicializace()

  ukaz_hadane(hadane_slovo, hadane_znaky)

  je_uhodnuto = False
  while zivoty > 0 and not je_uhodnuto:
    hadane_slovo, zivoty, hadane_znaky = cyklus_hry(hadane_slovo, zivoty, hadane_znaky)

    je_uhodnuto = True
    for pismeno in hadane_slovo:
      if pismeno not in hadane_znaky:
        je_uhodnuto = False

  if je_uhodnuto:
    print("Vyhrál jsi!!!")
    print("🎉🎉🎉")
    print("Slovo", hadane_slovo, "jsi uhodl na", 7 - zivoty + len(hadane_znaky), "pokusů")
  else:
    print("Prohrál jsi :(")
    print("Hádané slovo bylo:", hadane_slovo)


sibenice()