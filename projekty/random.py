import random


class Hod_minci_se_sazenim:
    def __init__(self, account):
        self.account = account


    def hod_minci(self):
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
            print("Tipni si (panna/orel):", end=" ")
            tip = input_check(input(), ["panna", "orel"])

            if self.hod_minci() == tip:
                print("Vyhravas ", money * 2, "!!", sep="")
                self.change_account_money(money*2)
                self.stav_uctu()
            else:
                print("Prohravas!!")
                self.stav_uctu()


    def stav_uctu(self):
        print("Stav uctu:", self.account, "Kc")


    def change_account_money(self, money):
        self.account += money


    def game(self):
        self.stav_uctu()

        self.gamble(input("Kolik ches vsadit? "))


def input_check(user_input, choices):
    if (user_input).lower() not in choices:
        print("bad input!!")
        return
    else:
        return user_input


hm_hrac = Hod_minci_se_sazenim(100)
play_again = True

while play_again:
    hm_hrac.game()
    if input_check(input("Hrat znovu [a/n]: "), ["a", "n"]) == "a":
        play_again = True
    else:
        play_again = False
    
    print("-----------------\n")