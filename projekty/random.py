import random
import itertools

players = []


class Coin_throw_bets:
    id_obj = itertools.count()


    def __init__(self, account):
        self.id = next(Coin_throw_bets.id_obj)
        self.account = account


    def Coin_throw(self):
        hod = random.choice([0,1])

        print("padlo:", end=" ")

        if hod == 1:
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

            if self.Coin_throw() == bet:
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
            if input_check("Hrat znovu", ["a", "n"]) == "a":
                play_again = True
            else:
                play_again = False

            print("-----------------\n")


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
                print(choice, end=" ")
            elif choice == choices[-1]:
                print(choice, end=": ")
            else:
                print(", " + choice)
    user_input = input().lower()
    while user_input not in choices:
        print("bad input!!")
        print(message, end=" ")
        user_input = input().lower()
    
    return user_input


def account_creation():
    choice = input_check("Co ches hrat?", ["hodminci"])

    if choice == "hodminci":
        players.append(Coin_throw_bets(100))


def game():
    account_creation()
    players[0].play()


game()