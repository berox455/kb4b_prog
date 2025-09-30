import random
import itertools

players = []


class Coin_throw:
    id_obj = itertools.count()


    def __init__(self, account):
        self.id = next(Coin_throw.id_obj) #if I wanted to create it with more players
        self.game_name = "coin_throw" #to tell games apart
        self.account = account #how much money player has for gambling


    def c_throw(self):
        throw = random.choice([0,1])

        print("padlo:", end=" ")

        if throw == 1:
            print("orel")
            return "orel"
        else:
            print("panna")
            return "panna"


    def gamble(self, money):
        if not money.isdigit():
            print("bad input!!")
            return

        money = int(money)

        if self.account < money:
            print("Vsazena castka je vetsi nez kolik mas penez!!!")
            return
        else:
            self.change_account_money(-money)
            bet = input_check("Tipni si", ["panna", "orel"])

            if self.c_throw() == bet:
                print("Vyhravas ", money * 2, "!!", sep="")
                self.change_account_money(money*2)
                self.account_money()
            else:
                print("Prohravas!!")
                self.account_money()


    def account_money(self):
        print("Stav uctu:", self.account, "Kc")


    def change_account_money(self, money):
        self.account += money


    def engine(self):
        self.account_money()
        self.gamble(input("Kolik ches vsadit? "))


    def play(self):
        play_again = True

        while play_again:
            if self.account < 1:
                print("Nemas uz penize ani na gamble!!!\nUmiras na hlad!!")
                return None
            self.engine()
            print("\n\n\n")
            if input_check("Hrat znovu hod minci?", ["a", "n"]) == "a":
                play_again = True
            else:
                play_again = False

            print("-----------------\n")


class Dice_throw:
    id_obj = itertools.count()
    

    def __init__(self):
        self.id = next(Dice_throw.id_obj)
        self.game_name = "dice_throw" #to tell games apart
        self.dice_count = 1
        self.dice_sides = 6

    
    def d_throw(self):
        throws = []

        for d in range(self.dice_count):
            throws.append(random.randrange(1, self.dice_sides + 1, 1))

        return throws
    

    def get_dice_count(self):
        dice_count = get_num("Zadej pocet kostek:")
        while dice_count < 1:
            dice_count = get_num("Zadej pocet kostek:")

        self.dice_count = dice_count
        

    def get_dice_sides(self):
        dice_sides = get_num("Zadej pocet sten kostky:")
        while dice_sides < 1:
            dice_sides = get_num("Zadej pocet sten kostky:")

        self.dice_sides = dice_sides
    

    def engine(self):
        throws = self.d_throw()
        th_n = len(throws) #number of throws

        if th_n < 2:
            print("Hod:", throws[0])
        elif th_n < 10001:
            print("Hody:", end=" ")

            for throw in throws:
                print(throw, end=" ")

            print("\nSoucet:", sum(throws))

        if len(throws) > 4:
            print("Prumerna hozena hodnota:", round(sum(throws)/th_n, 2))


    def play(self):
        play_again = True

        while play_again:
            self.get_dice_count()
            self.get_dice_sides()
            self.engine()

            if input_check("Hrat znovu hod kostkou?", ["a", "n"]) == "a":
                play_again = True
            else:
                play_again = False

            print("-----------------\n")


def get_num(message):
    print(message, end=" ")
    user_input = input()

    while not user_input.isdigit():
        print(message, end=" ")
        user_input = input()

    return int(user_input)


def input_check(message, choices):
    if message[-1] == "?":
        print(message, "Vyber ", end="")
    else:
        print(message + ",", "Vyber ", end="")

    if len(choices) == 1:
        print(choices[0], end=": ")
    elif len(choices) == 2:
        print(choices[0] + ",", choices[1], end=": ")
    else:
        for choice in choices:
            if choice == choices[0]:
                print(choice, end="")
            elif choice == choices[-1]:
                print(", " + choice, end=": ")
            else:
                print(", " + choice, end="")
    user_input = input().lower()
    while user_input not in choices:
        print("bad input!!")
        print(message, end=" ")
        user_input = input().lower()
    
    return user_input


def account_creation():
    choice = input_check("Co ches hrat?", ["hodminci", "hodkostkou"])

    if choice == "hodminci":
        players.append(Coin_throw(100))
    elif choice == "hodkostkou":
        players.append(Dice_throw())

def game():
    account_creation()
    players[0].play()
        
    print("Diky za hrani!!")


game()