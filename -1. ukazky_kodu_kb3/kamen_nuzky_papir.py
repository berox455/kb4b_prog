import random


hrac = input("Zadej kámen [k], nůžky [n], papír [p]:")[0]

hodnoty = ["p", "k", "n"]
if hrac not in hodnoty:
  print("Neplatný vstup!")
else:
  ai = random.choice(hodnoty)
  print("Oponent zahrál", ai)
  if ai == hrac:
    print("Remíza!")
  elif (ai == "p" and hrac == "n") or (ai == "n" and hrac == "k") or (ai == "k" and hrac == "p"):
    print("Vyhrál jsi!")
  else:
    print("Prohrál jsi!")