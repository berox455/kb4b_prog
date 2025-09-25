import math

def je_druha_mocnina(n):
  if n == 1:
    return True

  for i in range(n):
    if i*i == n:
      return True

  return False

def je_druha_mocnina_v2(n):
  return math.sqrt(n).is_integer()

def soucet_nizsich_mocnin(n, e):
  vysledek = 0
  for i in range(0, n+1):
    vysledek += i**e
  return vysledek

def je_dokonale(n):
  suma = 0
  for i in range(1, n):
    if n % i == 0:
      suma += i

  return suma == n

print(je_dokonale(6)) # True

print(je_dokonale(14)) # False

print(je_dokonale(28)) # True
