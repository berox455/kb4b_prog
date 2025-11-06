import random
from ulohy_random import get_num

def generuj_priklad():
    cislo1 = random.randint(0, 10)
    op = random.choice(["+", "-", "*"])
    cislo2 = random.randint(0, 10)

    print(f"{cislo1} {op} {cislo2} = ", end="")

    vstup = get_num()

    if op == "+":
        spravne = cislo1 + cislo2
    elif op == "-":
        spravne = cislo1 - cislo2
    else:
        spravne = cislo1 * cislo2

    return vstup == spravne

n_prikladu = 3
body = 0

for i in range(n_prikladu):
    if generuj_priklad():
        body += 1

print(f"Spravne: {body} / {n_prikladu}")