import random
import itertools
import string
import copy

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
            self.engine()
            if self.account < 1:
                print("Nemas uz penize ani na gamble!!!\nUmiras na hlad!!")
                break
            print("\n\n\n")
            if input_check("Hrat znovu hod minci?", ["a", "n"]) != "a":
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

            if input_check("Hrat znovu hod kostkou?", ["a", "n"]) != "a":
                play_again = False

        print("-----------------\n")


class Card_draw:
    id_obj = itertools.count()
    

    def __init__(self):
        self.id = next(Card_draw.id_obj)
        self.deck = [
            "♠A", "♠K", "♠Q", "♠J", "♠10", "♠9", "♠8", "♠7", "♠6", "♠5", "♠4", "♠3", "♠2",
            "♥A", "♥K", "♥Q", "♥J", "♥10", "♥9", "♥8", "♥7", "♥6", "♥5", "♥4", "♥3", "♥2",
            "♦A", "♦K", "♦Q", "♦J", "♦10", "♦9", "♦8", "♦7", "♦6", "♦5", "♦4", "♦3", "♦2",
            "♣A", "♣K", "♣Q", "♣J", "♣10", "♣9", "♣8", "♣7", "♣6", "♣5", "♣4", "♣3", "♣2"
            ]
        self.hand = []


    def c_draw(self):
        if len(self.deck) >= 1:
            card = random.choice(self.deck)
            self.deck.remove(card)

            return card
        else:
            return False


    def engine(self):
        card = self.c_draw()
        self.hand.append(card)

        if card == False:
            return False
        print("Vytahl jsi:", card)

        if len(self.hand) < 2:  
            print("V ruce:", self.hand[0])
        else:
            for card in self.hand:
                if card != self.hand[-1]:
                    print(card + ",", end=" ")
                else:
                    print(card)
    

    def play(self):
        play_again = True
        
        input("Pro vygenerovani karty zmackni enter...")
        while play_again and len(self.deck) > 0:
            self.engine()

            print("\n\n")

            if len(self.deck) < 1:
                print("Vycerpal jsi cely balicek karet!!!")
                play_again = False
                break
    
            if input_check("Vygenerovat dalsi kartu?", ["a", "n"]) != "a":
                play_again = False
        
        print("-----------------\n")


class Password_gen:
    id_obj = itertools.count()


    def __init__(self, pass_length = [12,18]):
        self.id = next(Password_gen.id_obj)
        self.game_name = "password_gen"
        self.pass_length = pass_length #min, max
        self.special_characters = list(string.punctuation)
        self.numbers = list(string.digits )
        self.password = ""
        self.alphabet = list(string.ascii_letters)


    def pass_check(self, password):
        bool_sp_ch = False #if there's a special character in the password
        bool_num = False #number
        bool_uc = False #uppercase letter

        check = bool_sp_ch and bool_num and bool_uc

        alphabet_uc = list(string.ascii_uppercase)

        for letter in password:
            if letter in self.special_characters:
                print("There's a special character!")
                bool_sp_ch = True
            if letter in self.numbers:
                print("There's a number character!")
                bool_num = True
            if letter in alphabet_uc:
                print("There's an uppercase character!")
                bool_uc = True
            check = bool_sp_ch and bool_num and bool_uc
            if check:
                break

        print("Check:", check)
        return check

    
    def generator(self):
        beta_password = ""
        while not self.pass_check(beta_password):
            beta_password = ""
            for i in range(random.randrange(self.pass_length[0], self.pass_length[1], step = 1)):
                beta_password += random.choice(self.alphabet + self.special_characters + self.numbers)

        self.password = beta_password

    
    def engine(self):
        self.generator()
        print("Vygenerovane heslo:", self.password)


    
    def play(self):
        play_again = True

        input("Pro vygenerovani hesla zmackni enter...")
        while play_again:
            self.engine()

            print("\n\n")

            if input_check("Vygenerovat dalsi heslo?", ["a", "n"]) != "a":
                play_again = False
        
        print("-----------------\n")


class Guess_the_number:
    id_obj = itertools.count()


    def __init__(self):
        self.id = next(Guess_the_number.id_obj)
        self.gnumber_range = [1,100] #min max
        self.gnumber = 0 #the number you're guessing
        self.guesses = 0 #number of guesses you have until you've guessed the number


    
    def num_gen(self):
        gnr = self.gnumber_range
        self.gnumber = random.randrange(gnr[0], gnr[1])


    def num_check(self, number):
        gnr = self.gnumber_range
        if number not in range(gnr[0], gnr[1]+1):
            print("Cislo neni v hadacim rozmezi!!!")
            return False
        
        return True


    def num_guesser(self):
        guess = get_num("Hadej cislo (1-100):")

        while not self.num_check(guess):
            guess = get_num("Hadej cislo (1-100):")

        if guess == self.gnumber:
            return True
        elif guess > self.gnumber:
            print("Moc vysoko!!")
        elif guess < self.gnumber:
            print("Moc nizko!!")

        return False


    def engine(self):
        self.num_gen()
        guessed = self.num_guesser()
        self.guesses = 1
        while not guessed:
            self.guesses += 1
            guessed = self.num_guesser()

        print("Uhodl jsi!! Pocet pokusu:", self.guesses)

    
    def play(self):
        play_again = True

        while play_again:
            self.engine()

            print("\n\n")

            if input_check("Hadat dalsi cislo?", ["a", "n"]) != "a":
                play_again = False
        
        print("-----------------\n")


class Poker_sim(Card_draw):
    id_obj = itertools.count()


    def __init__(self):
        super().__init__()
        self.id = next(Poker_sim.id_obj)
        self.table = []

    
    def gen_table(self):
        for i in range(2):
            card = super().c_draw()
            self.table.append(card)

    
    def gen_hand(self):
        for i in range(3):
            card = super().c_draw()
            self.hand.append(card)

    
    def get_value(self, card):
        facecard_value = {
            "A":14,
            "K":13,
            "Q":12,
            "J":11
        }            
        value = card[1:]
        if value in list("AKQJ"):
            #print(card, type(facecard_value[value])) #debug
            return facecard_value[value]
        else:
            #print(card, type(value)) #debug
            return int(value)

    
    def check_poker_hand(self):
        tph = self.table + self.hand #table plus hand
        tph = sorted(tph, key=self.get_value) #sort by value
        pair = False, None
        three = False, None #three of a kind
        four = False, None #four of a kind
        flush = True, tph
        straight = False, tph

        for card in tph:
            if card == tph[0]:
                most_value = [card]
            elif self.get_value(card) > self.get_value(most_value[0]):
                most_value = [card]
            elif self.get_value(card) == self.get_value(most_value[0]):
                most_value.append(card)
                if len(most_value) == 2:
                    pair = True, most_value.copy()
                elif len(most_value) == 3:
                    three = True, most_value.copy()
                elif len(most_value) == 4:
                    four = True, most_value.copy()

        tph = sorted(tph, key=self.get_value, reverse=True)

        if not pair[0] or not three[0] or not four[0] and len(tph) == 5:
            i = 1
            for card in tph:
                if i == len(tph):
                    break
                card2 = tph[i]
                if card[0] != card2[0]:
                    flush = False, tph
                    break
                i += 1

            straight_cards = 1
            j = 1
            for card in tph:
                if j == len(tph):
                    break
                card1 = self.get_value(card)
                card2 = self.get_value(tph[j])
                #print(card, "postupka", tph[j], card1 == card2 + 1) #debug
                if card1 == card2 + 1:
                    straight_cards += 1
                else:
                    straight_cards = 1
                j += 1

            if straight_cards >= 5:
                straight = True, tph
        else:
            flush = False, tph
            straight = False, tph
        
        if len(most_value) < 2:
            print("Nejvyssi karta:", most_value[0])
        else:
            print("Nejvyssi karty:", end=" ")
            for card in most_value:
                print(card, end=" ")
            print()

        if pair[0]:
            print("Par:", end=" ")
            self.print_cards(pair[1])
        if three[0]:
            print("Trojice:", end=" ")
            self.print_cards(three[1])
        if four[0]:
            print("Ctverice:", end=" ")
            self.print_cards(four[1])
        if flush[0]:
            print("Barva:", end=" ")
            self.print_cards(flush[1])
        if straight[0]:
            print("Postupka:", end=" ")
            self.print_cards(straight[1])
            return False #debug

        return True

    
    def print_cards(self, cards):
        for card in cards:
            print(card, end=" ")
        
        print()
            
    
    def play(self):
        self.gen_table()
        self.gen_hand()
        print("Na stole:", self.table) #debug
        print("V ruce:", self.hand) #debug

        if self.check_poker_hand() is False:
            return False


def get_num(message):
    print(message, end=" ")
    user_input = input()

    while not user_input.isdigit():
        print("bad input!!")
        print(message, end=" ")
        user_input = input()

    return int(user_input)


def input_check(message, choices):
    message_choices_print(message, choices)

    user_input = input().lower()
    while user_input not in choices:
        print("bad input!!")
        message_choices_print(message, choices)
        user_input = input().lower()
    
    return user_input


def message_choices_print(message, choices):
    if message[-1] == "?":
        print(message, "Vyber ", end="")
    else:
        print(message + ",", "Vyber ", end="")

    if len(choices) == 1:
        print(choices[0], end=": ")
    else:
        for choice in choices:
            if choice != choices[-1]:
                print(choice + ",", end=" ")
            else:
                print(choice, end=": ")


def account_creation(debug = False, debug_game = None):
    if debug:
        choice = debug_game
    else:
        choice = input_check("Co ches hrat?", ["hodminci", "hodkostkou", "genkarty", "genhesla", "hadejcislo", "simpokru", "nechcihrat"])

    if choice == "hodminci":
        players.append(Coin_throw(100))
    elif choice == "hodkostkou":
        players.append(Dice_throw())
    elif choice == "genkarty":
        players.append(Card_draw())
    elif choice == "genhesla":
        players.append(Password_gen())
    elif choice == "hadejcislo":
        players.append(Guess_the_number())
    elif choice == "simpokru":
        players.append(Poker_sim())


    else:
        return False

    return True


def game():
    go = account_creation(True, "simpokru") #debug
    i = 0

    while go:
        if players[i].play() is False:
            break
        go = account_creation(True, "simpokru") #debug
        i += 1
        
    print("Diky za hrani!!")

game()