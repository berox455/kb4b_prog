def pocet_samohlasek(slovo):
  pocet = 0
  samohlasky = ["a","e","i","o","u"]
  slovo = slovo.lower()

  for znak in slovo:
    if znak in samohlasky:
      pocet += 1

  return pocet


print( pocet_samohlasek("Anna"))