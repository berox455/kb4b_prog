import random
from ulohy_random import get_num
from time import sleep

def generuj_priklad(priklad):
    cislo1 = int(priklad.split()[0])
    op = priklad.split()[1]
    cislo2 = int(priklad.split()[2])

    print(f"{priklad} =", end=" ")

    vstup = int(input())

    if op == "+":
        spravne = cislo1 + cislo2
    elif op == "-":
        spravne = cislo1 - cislo2
    else:
        spravne = cislo1 * cislo2

    return vstup == spravne

cesta = "2. prace_se_soubory/data/priklady.txt"

with open(cesta, "r") as file:
    priklady = file.readlines()

    i = 0
    for p in priklady:
        nova = p.strip()

        priklady[i] = nova
        i += 1

    n_prikladu = 3
    body = 0

    for i in range(n_prikladu):
        if generuj_priklad(random.choice(priklady)):
            body += 1

print(f"Spravne: {body} / {n_prikladu}")