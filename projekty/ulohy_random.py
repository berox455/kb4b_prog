import random
import itertools
import string
import copy
from time import sleep
import re

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
                #print("There's a special character!")
                bool_sp_ch = True
            if letter in self.numbers:
                #print("There's a number character!")
                bool_num = True
            if letter in alphabet_uc:
                #print("There's an uppercase character!")
                bool_uc = True
            check = bool_sp_ch and bool_num and bool_uc
            if check:
                break

        #print("Check:", check)
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
        self.table = []
        for i in range(3):
            card = super().c_draw()
            self.table.append(card)

    
    def gen_hand(self):
        self.hand = []
        for i in range(2):
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
            return facecard_value[value]
        else:
            return int(value)

    
    def get_list_value(self, clist):
        vlist = []

        for card in clist:
            vlist.append(self.get_value(card))

        return vlist


    def hc_pair_three_four(self, tph): 
    #checks for high card, pair three of a kind and four of a kind, needs a list of cards available (tph)
    #returns a list of lists: [most_value_cards],  [pair_bool, pair_cards], three, four (devided like pair)
        tph = sorted(tph, key=self.get_value) #sort by value low to high
        pair = False, None
        three = False, None #three of a kind
        four = False, None #four of a kind

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

        return most_value, pair, three, four


    def flush_straight(self, tph):
        #checks for flush and straight
        #returns list of lists: [flush_bool, flush_cards], [straight_bool, straight_cards]
        tph = sorted(tph, key=self.get_value, reverse=True) #sorted by value high to low
        flush = False, tph
        straight = False, tph

        scs = [] #suit cards
        hcs = []
        dcs = []
        ccs = []

        for card in tph:
            match card[0]:
                case "♠":
                    scs.append(card)
                case "♥":
                    hcs.append(card)
                case "♦":
                    dcs.append(card)
                case "♣":
                    ccs.append(card)

            if len(scs) >= 5:
                flush = True, scs[:4]
                break
            if len(hcs) >= 5:
                flush = True, hcs[:4]
                break
            if len(dcs) >= 5:
                flush = True, dcs[:4]
                break
            if len(ccs) >= 5:
                flush = True, ccs[:4]
                break

            


        n_straight_cards = 1
        j = 1
        tph_value = 0
        for card in tph:
            card1 = self.get_value(card)
            tph_value += card1
            if j == len(tph):
                break
            card2 = self.get_value(tph[j])
            if card1 == card2 + 1:
                n_straight_cards += 1
                print("Straight trig:", n_straight_cards) #debug
            elif len(tph) > 5 and card1 == card2:
                n_straight_cards = n_straight_cards
            else:
                n_straight_cards = 1
            j += 1

        if n_straight_cards >= 5:
            straight = True, tph
        elif tph_value == 28 and self.get_value(tph[0]) == 14:
            k = 2
            for card in tph[1:]:
                if k == len(tph):
                    straight = True, tph[1:] + [tph[0]]
                    break
                card1 = self.get_value(card)
                card2 = self.get_value(tph[k])
                if card1 != card2 + 1:
                    break
                k += 1
        
        return flush, straight


    def fullhouse_twopair(self, tph):
        #checks for a full house and two pair
        #returns a list of lists: [fullhouse_bool, fullhouse_cards], [twopair_bool, twopair_cards]
        tph = sorted(tph, key=self.get_value, reverse=True)
        twopair = False, [None]
        fullhouse = False, tph

        pair_cards = []
        toak_cards = []

        tphlist_value = self.get_list_value(tph)

        i = 0
        for value in tphlist_value:
            tlv = tphlist_value.copy()
            tlv.remove(value)
            if value in tlv:
                #there is a pair
                pair_cards.append(tph[i])
                tlv.remove(value)
            
            if value in tlv:
                #there is a three of a kind
                toak_cards.append(tph[i])
                if len(pair_cards) > 2:
                    pair_cards.remove(tph[i])
            
            if len(toak_cards) > 3:
                toak_cards.remove(tph[i])

            i += 1
        
        if len(pair_cards) > 3 and sum(self.get_list_value(pair_cards[:1])) != sum(self.get_list_value(pair_cards[2:3])):
            twopair = True, pair_cards
        if len(toak_cards) > 1 and len(pair_cards) > 2:
            fullhouse = True, toak_cards[:2] + pair_cards[2:3]

        return fullhouse, twopair

    
    def straightflush(self, tph):
    #checks for straightflushes
        fs = self.flush_straight(tph)
        flush = fs[0]
        straight = fs[1]

        if flush[0] and straight[0]:
            return True, straight[1]
        else:
            return False, tph

    
    def royalflush(self, tph):
    #checks for royalflushes
        sf = self.straightflush(tph)
        cards = sf[1]

        if sf[0] and self.get_value(cards[0]) == 14:
            return True, cards
        else:
            return False, tph


    
    def check_poker_hand(self):
        tph = self.table + self.hand #table plus hand

        hptf = self.hc_pair_three_four(tph)
        most_value = hptf[0]
        pair = hptf[1]
        three = hptf[2]
        four = hptf[3]
        twopair = False, [None]
        fullhouse = False, tph
        flush = False, tph
        straight = False, tph
        straightflush = False, tph
        royalflush = False, tph
            
        if not pair[0] and len(tph) == 5:
            fs = self.flush_straight(tph)
            flush = fs[0]
            straight = fs[1]
        elif pair[0] or len(tph) >= 5:
            straight = fs[1]
            fhtp = self.fullhouse_twopair(tph)
            fullhouse = fhtp[0]
            twopair = fhtp[1]

        if straight[0]:
            straightflush = self.straightflush(tph)
            if straightflush[0]:
                royalflush = self.royalflush(tph)
            
            
        
        print("Nejvyssi karta:", most_value[0])
        if pair[0]:
            print("Par:", end=" ")
            self.print_cards(pair[1])
        if twopair[0]:
            print("Dva pary:", end=" ")
            self.print_cards(twopair[1])
        if three[0]:
            print("Trojice:", end=" ")
            self.print_cards(three[1])
        if straight[0]:
            print("Postupka:", end=" ")
            self.print_cards(straight[1])
        if flush[0]:
            print("Barva:", end=" ")
            self.print_cards(flush[1])
            return False #debug
        if fullhouse[0]:
            print("Fullhouse:", end=" ")
            self.print_cards(fullhouse[1])
        if four[0]:
            print("Ctverice:", end=" ")
            self.print_cards(four[1])
        if straightflush[0]:
            print("Cista postupka:", end=" ")
            self.print_cards(straightflush[1])
        if royalflush[0]:
            print("Kralovska postupka:", end=" ")
            self.print_cards(royalflush[1])

        return True

    
    def print_cards(self, cards):
        for card in cards:
            print(card, end=" ")
        
        print()

    def print_table(self):
        j = str((self.table)).replace("\'", "")
        j = j.replace(", ", "")
        j = j.strip("y[]")
        lj = (len(j)) + len(self.table) + 1
        for i in range(lj):
            print("_", end="")

        print("\n ", end="")
        self.print_cards(self.table)

        for i in range(lj):
            print("_", end="")
        
        print()

    
    def engine(self):
        self.print_table()
        print("\nV ruce:", end=" ")
        self.print_cards(sorted(self.hand, key=self.get_value, reverse=True))
        print("\n___________________________________")
        if self.check_poker_hand(): #debug
            return True #debug


    def play(self):
        self.gen_table()
        self.gen_hand()
        self.engine()
        add_card = "a" #input_check("\n\nOtocit kartu na stole?", ["a", "n"]) #debug
        
        while add_card == "a":
            self.table.append(super().c_draw())
            if self.engine(): #debug
                eret = True #debug
            else:
                eret = False
            if len(self.table) == 5:
                print("\nVsechny karty na stole jsou otoceny")
                break
            add_card = "a" #input_check("\n\nOtocit kartu na stole?", ["a", "n"]) #debug
            
        print("-----------------------------------\n")
        return eret #debug


def get_num(message=""):
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
        choice = input_check("Co ches hrat?", [
            "hodminci", "hodkostkou", "genkarty", 
            "genhesla", "hadejcislo", "simpokeru", 
            "nechcihrat"
            ])

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
    elif choice == "simpokeru":
        players.append(Poker_sim())


    else:
        return False

    return True


def game():
    go = account_creation()#True, "simpokeru") #debug
    i = 0

    while go:
        if players[i].play() is False:
            break
        go = account_creation()#True, "simpokeru") #debug
        i += 1
        
    print("Diky za hrani!!")

game()
#
#u = Card_draw()
#
#x_deck = []
#
#for i in u.deck:
#    x = re.findall("0$", i)
#    if x:
#        x_deck.append(i)
#
#print(x_deck)

#in pokersim change in func flushstraigh and hcptf when looping through thp loop in thplist_value instead
#because you don't have to then use self.get_value so many times and 
#the code will be better and more beautiful and also shorter i think
