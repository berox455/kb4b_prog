import csv
import random
import matplotlib.pyplot as plt
import os
from helpful import input_check, message_choices_print

path = "projekty/cichnaonar/"  # path to the project without a file
username = ""

def write_user(path: str) -> bool:
    if not os.path.isfile(path+"login.csv"):
        clear_login_file(path)
        return False
    else:
        name, password = create_user()
        print(f"name: {name}, password: {password}")
        if input("Is this information correct? [y][n]\t").lower() != "y":
            return False

        with open(path + "login.csv", "a") as file:
            file.write(f"{name},{password}\n")
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


def add_winner(path) -> None:
    path = path + "winners.csv"
    if not os.path.isfile(path):
        with open(path, "w") as file:
            file.write("name\n")

    with open(path, "a") as file:
        file.write(f"{username}\n")


def competition() -> None:
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
    else:
        add_winner(path)
        print("You won!!")


    return None


def print_winners(path) -> None:
    path = path + "winners.csv"
    winners: list[str] = []

    with open(path, "r") as file:
        reader = csv.DictReader(file)

        for line in reader:
            winners.append(line["name"])

    if len(winners) > 0:
        print("The winners are:")
        for winner in winners:
            if winner == winners[-1]:
                print(winner)
            else:
                print(winner, end=", ")
    else:
        print("There are no winners yet! You can be the first!")


def engine() -> None:
    choice = input_check("Now the main part of the game", ["statistics", "winners", "play", "exit"])
    match choice:
        case "statistics":
            get_graphs()
        case "winners":
            print_winners(path)
        case "play":
            competition()
            print("Game's not done yet!!!")
        case _:
            return None


def game() -> None:
    auth = authentication()

    if auth:
        print("Welcome to cichnaonar!!!")
        engine()
        print("Thanks for playig!!")


game()
#register()
#login(path)
#clear_login_file(path)
