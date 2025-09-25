cislo1 = int(input("Zadej první číslo: "))
cislo2 = int(input("Zadej druhé číslo: "))

op = input("Zadej operaci [+, -, *, /]: ")

if (op == "+"):
  print("Součet:", cislo1 + cislo2)
elif (op == "-"):
  print("Rozdíl:", cislo1 - cislo2)
elif (op == "*"):
  print("Násobek:", cislo1 * cislo2)
elif (op == "/"):
  print("Podíl:", cislo1 / cislo2)
else:
  print("Neplatný vstup.")