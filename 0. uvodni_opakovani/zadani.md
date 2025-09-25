# Po-prázdninový Python refresher

Zadání řešte pomocí tvorby funkcí.

Nebojte se googlovat a hledat programátorské rady :)

### Vypsání dělitelů
Vytvoř funkci, která na vstupu bere číslo. Následně vypíše všechny dělitele tohoto čísla.
 Např.
 - vstup: 12
 - výstup:
    1
    2
    3
    4
    6
    12

### Vykreslení schodů
 Načti číslo udávající výšku a znak. Následně z tohoto znaku vykresli schody o dané výšce.

 Např.
 - vstup: 5 "h"
 - výstup:<br>
    h<br>
    hh<br>
    hhh<br>
    hhhh<br>
    hhhhh

### Validátor rodného čísla:
Uživatel zadá řetězec. Zjisti, zda se jedná o validní rodné číslo.
- pokud ANO - vypiš datum narození uživatele a jeho pohlaví
- pokud NE - ukonči program
![tahak k datu narození](helpers/datum-narozeni-1404272651.jpg)
 Např.
 - vstup: 850126/1158
 - výstup:
    *Validní rodné číslo*
    *26.1.1985*
    *Muž*

### Validátor vstupu:
Uživatel musí na vstupu zadat libovolné kladné třímístného sudé číslo. Pokud uživatel zadá špatný vstup, podej mu chybovou hlášku a načítej vstup znovu (dokud nezadá vstup správný.)

### Vymazání duplicit
Vytvoř funkci, který na vstupu dostane pole čísel. Následně z tohoto pole vymaže veškeré duplicity.
 Např.
 - vstup: [3, 1, 3, 2, 1, 3]
 - výstup: [3, 1, 2]

### Validace e-mailu
Vytvoř funkci, která na vstupu vezme emailovou adresu a zkontroluje, zda je validní
Validní e-mail je takový, který:
- obsahuje právě jeden znak @
- před @ má aspoň jeden znak
- za  @ má alespoň jeden znak . alespoň jeden znak

# Těžší příklad:

### Generátor sudoku
Vytvoř funkci, která je schopna náhodně generovat zadání pro sudoku. Funkce na vstupu dostane jedinou proměnou *komplet* typy *Bool*
- pokud *komplet=True* vypiš kompletní řešení generovaného sudoku
- pokud *komplet=False* vypiš pouze polovinu číslic ze zadání.