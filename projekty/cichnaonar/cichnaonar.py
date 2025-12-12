import csv
import random
import matplotlib.pyplot as plt
import os
from helpful import input_check, message_choices_print

path = "projekty/cichnaonar/"  # path to the project without a file
username = ""
other_user_data: list[str] = []

def write_user(path: str) -> bool:
    if not os.path.isfile(path+"login.csv") or not os.path.isfile(path+"winners.csv"):
        clear_login_file(path)
        clear_winners_file(path)
        return False
    else:
        name, password = create_user()
        print(f"name: {name}, password: {password}")
        if input("Is this information correct? [y][n]\t").lower() != "y":
            return False

        with open(path + "login.csv", "a") as file:
            file.write(f"{name},{password}\n")
        with open(path + "winners.csv", "a") as file:
            file.write(f"{name},0,0,,0")
    return True


def create_user() -> tuple[str, str]:
    name = input("Enter a username: ")
    p0, p1 = get_pass()
    same_pass = p0 == p1
    while not same_pass:
        print("password are not the same, try again!")
        p0, p1 = get_pass()
        same_pass = p0 == p1
    return name, p0


def get_pass() -> tuple[str, str]:
    password = input("Enter a password: ")
    password1 = input("Enter the password again: ")

    return password, password1
    

def register() -> None:
    register_bool = write_user(path)
    while not register_bool:
        register_bool = write_user(path)


def login(path: str) -> bool:
    path = path + "login.csv"
    global username
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    with open(path, "r") as file:
        reader = csv.DictReader(file)

        for line in reader:
            if username == line["username"] and password == line["password"]:
                print("You logged in successfully")
                return True
    print("Wrong username or password!!!")
    return False


def get_questions(path) -> tuple[list, list, list]:
    path = path + "quiz_questions.csv"
    e_questions: list = []
    m_questions: list = []
    h_questions: list = []

    with open(path, "r") as file:
        reader = csv.DictReader(file)

        for line in reader:
            match line["difficulty"]:
                case "easy":
                    e_questions.append(line)
                case "medium":
                    m_questions.append(line)
                case "hard":
                    h_questions.append(line)

    """ Debug print
    print("easy")
    for q in e_questions:
        print(q["difficulty"], q["category"])
    print("medium")
    for q in m_questions:
        print(q["difficulty"], q["category"])
    print("hard")
    for q in h_questions:
        print(q["difficulty"], q["category"])
    """

    return e_questions, m_questions, h_questions


def stats(path) -> tuple[list[str], list[int], list[str], list[int]]:
    e, m, h = get_questions(path)
    path = path + "quiz_questions.csv"

    diffs = ["easy", "medium", "hard"]
    n_diffs = [len(e), len(m), len(h)]


    categories: list[str] = []
    n_categories: list[int] = []

    with open(path, "r") as file:
        reader = csv.DictReader(file)


        for line in reader:
            category = line["category"]
            if category not in categories:
                categories.append(category)
                n_categories.append(1)
            
            for index, name in enumerate(categories):
                if category == name:
                    n_categories[index] += 1

    return diffs, n_diffs, categories, n_categories


def get_graphs() -> None:
    diffs, n_diffs, categories, n_categories = stats(path)



    for index, name in enumerate(diffs):
        print(f"{name}: {n_diffs[index]}")
    plt.bar(diffs, n_diffs)
    plt.title("Difficulty ratio")
    plt.xlabel("Difficulty")
    plt.ylabel("# of Questions")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

    for index, name in enumerate(categories):
        print(f"{name}: {n_categories[index]}")
    plt.bar(categories, n_categories)
    plt.title("Category ratio")
    plt.xlabel("Categories")
    plt.ylabel("# of Questions")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


def clear_login_file(path) -> None:  # debug
    path = path + "login.csv"
    with open(path, "w") as file:
        file.write("username,password\n")


def clear_winners_file(path) -> None:
    path = path + "winners.csv"
    with open(path, "w") as file:
        file.write("name,plays,wins,games,last_lvl_reached\n")


def authentication() -> bool:
    choice = input_check("Create an account or log in to an existing one", ["register", "login"])
    auth = False
    match choice:
        case "register":
            register()
        case "login":
            auth = login(path)
        case _:
            print("Something went wrong!!!!!!!")

    return auth


def pick_question(questions_from_difficulty: list) -> tuple[dict, bool]:
    qfd = questions_from_difficulty

    question = random.choice(qfd)

    question_cat = question["category"]
    question_txt = question["question"]

    print(f"Category: {question_cat}")
    print(question_txt)

    if question["correct_answer"] == "True":
        question_bool = True
    else:
        question_bool = False

    return question, question_bool


def get_user(path) -> tuple[str, int, int, str, int]:
    path = path + "winners.csv"
    name = username
    plays = 0
    wins = 0
    games = ""
    last_lvl_reached = 0

    with open(path, "r") as file:
        reader = csv.DictReader(file)

        for line in reader:
            if line["name"] != name:
                temp = ""
                for n in line:
                    if n != line[0]:
                        temp += "," + n[1]
                    else:
                        temp += n[1]
                other_user_data.append(temp)
                continue
            
            plays = int(line["plays"])
            wins = int(line["wins"])
            games = line["games"]
            last_lvl_reached = int(line["last_lvl_reached"])

    return name, plays, wins, games, last_lvl_reached


def save_user(path, game: str, last_lvl_reached: int) -> None:
    name, plays, wins, games, not_useful_now = get_user(path)
    games += game

    clear_winners_file(path)

    path += "winners.csv"

    if game == "T":
        wins += 1
    plays += 1


    with open(path, "a") as file:
        for string in other_user_data:
            file.write(f"{string}\n")
        file.write(f"{name},{plays},{wins},{games},{last_lvl_reached}\n")
        


def competition() -> int:
    questions = get_questions(path)
    lvl = 1
    os.system('cls' if os.name == 'nt' else 'clear')

    while lvl < 15:
        print(f"Lvl {lvl}")
        pick, question_bool = pick_question(questions[(lvl-1)//5])
        questions[(lvl-1)//5].remove(pick)

        answer = input_check("True or False?", ["true", "false"])
        if answer == "true":
            answer = True
        else:
            answer = False

        if answer != question_bool:
            print(f"It was in fact not {answer}")
            break
        
        print("That's right!")
        lvl += 1

    #add_winner(path)  # debug
    
    if lvl != 15:
        print("GG, better luck next time!!!")
        save_user(path, "F", lvl)
    else:
        save_user(path, "T", lvl)
        print("You won!!")

    return lvl


def print_winners(path) -> None:
    path = path + "winners.csv"
    winners: list[str] = []

    with open(path, "r") as file:
        reader = csv.DictReader(file)

        for line in reader:
            name = line["name"]
            if int(line["wins"]) >= 1:
                winners.append(name)

    if len(winners) > 0:
        print("The winners are:")
        for winner in winners:
            if winner == winners[-1]:
                print(winner)
            else:
                print(winner, end=", ")
    else:
        print("There are no winners yet! You can be the first!")


def player_stats(path) -> None:
    name, plays, wins, games, lats_lvl_reached = get_user(path)
    plays_ot: list[int] = []
    wins_ot: list[int] = []

    if plays == 0:
        print("You've never played!! \nPlay a game or two to see some stats!!")
        return None

    for game in games:
        if game == games[0]:
            wins_ot.append(0 if game == "F" else 1)
            plays_ot.append(1)
        else:
            plays_ot.append((plays_ot[-1] + 1))  # just do it in a seperate cycle
            wins_ot.append(wins_ot[-1] if game == "F" else wins_ot[-1] + 1)
            #if game == "T":
            #    wins_ot.append(wins_ot[-1] + 1)
            #else:
            #    wins_ot.append(wins_ot[-1])

    print(plays_ot, wins_ot)

    winrate = wins/plays
    print(f"plays: {plays}")
    print(f"wins: {wins}")
    print(f"winrate: {round(winrate*100, 2)}%")

    plt.plot(plays_ot, wins_ot)
    plt.title("Your stats")
    plt.ylabel("Wins")
    plt.xlabel("Plays")
    plt.xticks(plays_ot[::1])
    plt.yticks(wins_ot[::1])
    plt.show()


def statistics() -> None:
    choice = input_check("Your stats or game stats?", ["game", "user"])

    if choice == "user":
        player_stats(path)
    else:
        get_graphs()


def engine() -> None:
    choice = input_check("Now the main part of the game", ["stats", "winners", "play", "exit"])
    match choice:
        case "stats":
            statistics()
        case "winners":
            print_winners(path)
        case "play":
            competition()
        case _:
            return None


def game() -> None:
    auth = authentication()

    if auth:
        print("Welcome to cichnaonar!!!")
        engine()
        print("Thanks for playing!!")

#clear_winners_file(path)
game()
#register()
#login(path)
#clear_login_file(path)

""" winners rework
name, plays, wins, last lvl reached

anytime you run this code, it checks for winners.csv file
if it's not present, it creates it
if it is though, it copies it all and at the end if the user played the game
it adds the stats from it into the copy and then rewrites winners.csv with the new info

how do the stats work?
- they wouldn't be able to show progression through time
- it would take less time to show
- winrate would still be there
- wins and plays as well

is it better?
- the progression is pretty crucial, so probably not
- last level reached is pretty cool though

JUST add a list of bools to the file as games tab
so it's:

name: str, plays: int, wins: int, games: list[bool], last lvl reached: int
"""
