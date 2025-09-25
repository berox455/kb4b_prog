import random


# náhodné číslo z intervalu <0, 1>
val1 = random.random()
print(val1)

# náhodné číslo mezi 1 a 6 (včetně)
val2 = random.randint(1, 6)
print(val2)

# náhodná hodnota z pole
pole = ["♠", "♥", "♦", "♣"]
val3 = random.choice(pole)
print(val3)
