import csv
import random
import matplotlib.pyplot as plt
import os
from helpful import input_check, clear_terminal, hash_it
from time import sleep
from getpass import getpass

USER_LOGINS = "login.csv"
USER_SAVES = "winners.csv"
QUIZ_QUESTIONS = "quiz_questions.csv"
CURRENT_USER = "current_user.txt"


def write_user() -> bool:
    if not os.path.isfile(USER_LOGINS) or not os.path.isfile(USER_SAVES):
        clear_login_file()
        clear_winners_file()
        return False

    name, password = create_user()

    with open(USER_LOGINS, "a") as file:
        file.write(f"{name},{hash_it(password)}\n")
    with open(USER_SAVES, "a") as file:
        file.write(f"{name},0,0,,0")

    return True


def create_user() -> tuple[str, str]:
    name = input("Enter a username: ")
    p0, p1 = get_user_pass()
    same_pass = p0 == p1
    while not same_pass:
        print("password are not the same, try again!")
        p0, p1 = get_user_pass()
        same_pass = p0 == p1
    return name, p0


def get_user_pass() -> tuple[str, str]:
    password =  getpass("Enter a password: ")
    password1 = getpass("Enter the password again: ")

    return password, password1


def register() -> None:
    register_bool = write_user()
    while not register_bool:
        register_bool = write_user()


def login() -> bool:
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")
    password = hash_it(password)

    with open(USER_LOGINS, "r") as file:
        reader = csv.DictReader(file)

        for line in reader:
            if username == line["username"] and password == line["password"]:
                with open(CURRENT_USER, "w") as file:
                    file.write(username)
                print("You logged in successfully")
                sleep(1.5)
                clear_terminal()
                return True
    print("Wrong username or password!!!")
    return False


def get_questions() -> tuple[list, list, list]:
    e_questions: list = []
    m_questions: list = []
    h_questions: list = []

    with open(QUIZ_QUESTIONS, "r") as file:
        reader = csv.DictReader(file)

        for line in reader:
            match line["difficulty"]:
                case "easy":
                    e_questions.append(line)
                case "medium":
                    m_questions.append(line)
                case "hard":
                    h_questions.append(line)

    return e_questions, m_questions, h_questions


def stats() -> tuple[list[str], list[int], list[str], list[int]]:
    e, m, h = get_questions()
    diffs = ["easy", "medium", "hard"]
    n_diffs = [len(e), len(m), len(h)]

    categories: list[str] = []
    n_categories: list[int] = []

    with open(QUIZ_QUESTIONS, "r") as file:
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
    diffs, n_diffs, categories, n_categories = stats()

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


def clear_login_file() -> None:
    with open(USER_LOGINS, "w") as file:
        file.write("username,password\n")


def clear_winners_file() -> None:
    with open(USER_SAVES, "w") as file:
        file.write("name,plays,wins,games,last_lvl_reached\n")


def authentication() -> bool:
    text = "Create an account or log in to an existing one"
    choice = input_check(text, ["register", "login"])
    auth = False
    match choice:
        case "r":
            register()
        case "l":
            auth = login()
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

    question_bool = question["correct_answer"] == "True"

    return question, question_bool


def get_user() -> tuple[dict, list[dict]]:
    user_data = {
    "name":"",
    "plays": 0,
    "wins": 0,
    "games": "",
    "last_lvl_reached": 0
    }
    other_user_data: list[dict] = []
    with open(CURRENT_USER, "r") as file:
        user_data["name"] = file.readline()

    with open(USER_SAVES, "r") as file:
        reader = csv.DictReader(file)

        for line in reader:
            temp: dict = {}
            temp["name"] = line["name"]
            temp["plays"] = int(line["plays"])
            temp["wins"] = int(line["wins"])
            temp["games"] = line["games"]
            temp["last_lvl_reached"] = int(line["last_lvl_reached"])
            if line["name"] != user_data["name"]:
                other_user_data.append(temp)
            else:
                user_data = temp

    return user_data, other_user_data


def save_user(game: str, last_lvl_reached: int) -> None:
    user_data, other_user_data = get_user()
    user_data["games"] += game

    #clear_winners_file()

    if game == "T":
        user_data["wins"] += 1
    user_data["plays"] += 1

    user_data["last_lvl_reached"] = last_lvl_reached

    with open(USER_SAVES, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name","plays","wins","games","last_lvl_reached"])
        writer.writeheader()
        for line in other_user_data:
            writer.writerow(line)
        writer.writerow(user_data)


def competition() -> None:
    questions = get_questions()
    lvl = 0

    clear_terminal()

    while lvl < 15:
        print(f"Lvl {lvl+1}")
        pick, question_bool = pick_question(questions[(lvl)//5])
        questions[(lvl)//5].remove(pick)

        answer = input_check("True or False?", ["t", "f"])
        answer = answer == "t"

        if answer != question_bool:
            print(f"It was in fact not {answer}")
            break

        print("That's right!")
        lvl += 1
        sleep(1)

    if lvl != 15:
        print("GG, better luck next time!!!")
        save_user("F", lvl)
    else:
        save_user("T", lvl)
        clear_terminal()

        print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⡆⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀
⠀⠀⠀⠠⢤⣦⠤⠀⠀⠉⢏⠀⠠⣤⣦⠄⠀⡸⠁⠀⠀⠀⣠⠹⠛⠏⠀⠀⠀⠀
⠀⣠⠀⠀⠉⠈⠐⢄⠀⠀⠈⢆⠀⠉⡏⠀⠰⠁⠀⠀⠠⠊⠀⠀⠠⢤⣦⡤⠀⠀
⠘⠛⠋⠒⠂⠤⢀⠀⠁⠀⣀⠀⠀⠀⠣⢤⣦⡤⠀⠁⠀⡀⠤⠒⠉⠈⠈⠁⠀⠀
⠀⠀⢠⣶⡄⠀⣀⣀⠀⠙⠛⢋⡀⠀⠀⡸⠉⠁⠀⠀⣁⡀⠠⠤⠄⠾⠷⠂⠀⠀       
,--.   ,--.,-----. ,--. ,--.    ,--.   ,--.,--.,--.  ,--. 
 \  `.'  /'  .-.  '|  | |  |    |  |   |  ||  ||  ,'.|  | 
  '.    / |  | |  ||  | |  |    |  |.'.|  ||  ||  |' '  | 
    |  |  '  '-'  ''  '-'  '    |   ,'.   ||  ||  | `   | 
    `--'   `-----'  `-----'     '--'   '--'`--'`--'  `--' 
                    ⣀⣤⣀⢀⣀⣀⠀⠀⠀⠀⠀⠀⠈⠀⠐⠀⠀⠀⠁⢤⣶⡄⠀⠀⣀⣀⡀⣀⣠⣀
                    ⠘⠉⠁⠀⠀⠀⢀⡠⠄⠂⠀⡠⠀⠀⠀⠐⢄⠀⠀⠂⠠⠄⣀⠀⠀⠀⠀⠘⠛⠃
                    ⠀⠀⠀⣶⣶⠉⠁⠀⢀⣄⠞⠀⠀⠀⡄⠀⠀⠑⠄⡀⠀⠀⠀⠉⢳⣾⡖⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠃⠀⠠⣴⣦⠄⠀⠈⠝⠛⠅⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                          
""")


def print_winners() -> None:
    winners: list[str] = []

    with open(USER_SAVES, "r") as file:
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


def player_stats() -> None:
    user_data, other_user_data = get_user()
    plays_ot: list[int] = []
    wins_ot: list[int] = []
    text1 = "You've either never played or played only once!!"
    text2 = "Play a game or two to see some stats!!"

    name, plays, wins, games, last_lvl_reached = user_data.values()
    #print(name,plays,wins,games,last_lvl_reached)

    if plays <= 1:
        print(f"{text1}\n{text2}")
        return None

    for i in range(len(games)):
        plays_ot.append(i + 1)

    for index, game in enumerate(games):
        if index == 0:
            wins_ot.append(0 if game == "F" else 1)
        else:
            wins_ot.append(wins_ot[-1] if game == "F" else wins_ot[-1] + 1)

    winrate = wins/plays
    print(f"plays: {plays}")
    print(f"wins: {wins}")
    print(f"winrate: {round(winrate*100, 2)}%")
    print(f"last_lvl_reached: lvl {last_lvl_reached}")

    plt.plot(plays_ot, wins_ot)
    plt.title("Your stats")
    plt.ylabel("Wins")
    plt.xlabel("Plays")
    plen = len(plays_ot)
    if plen < 25:
        plt.xticks(plays_ot[::1])
    elif plen < 100:
        plt.xticks(plays_ot[::5])
    elif plen < 500:
        plt.xticks(plays_ot[::10])
    else:
        plt.xticks(plays_ot[::50])
    plt.yticks(wins_ot[::1])
    plt.show()


def statistics() -> None:
    choice = input_check("Your stats or game stats?", ["game", "user"])

    if choice == "user"[0]:
        player_stats()
    else:
        get_graphs()


def engine() -> bool:
    choices = ["stats", "winners", "play", "exit"]
    user_choice = input_check("Main game menu", choices)
    match user_choice:
        case "s":
            statistics()
        case "w":
            print_winners()
        case "p":
            competition()
        case _:
            return False
    return True


def game() -> None:
    auth = authentication()

    if auth:
        print("Welcome to cichnaonar!!!")
        running = engine()
        while running:
            running = engine()
        os.remove(CURRENT_USER)
        print("Thanks for playing!!")


game()
  # add a partial input possibility to main menu and other choices
  # test win
