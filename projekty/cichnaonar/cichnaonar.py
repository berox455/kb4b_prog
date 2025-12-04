import csv
import random
import matplotlib.pyplot as plt
import os.path
from helpful import input_check, message_choices_print

path = "projekty/cichnaonar/"  # path to the project without a file

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
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    with open(path, "r") as file:
        reader = csv.DictReader(file)

        for line in reader:
            if username == line["username"] and password == line["password"]:
                print("You logged in successfully")
                return True
    return False


def clear_login_file(path) -> None:  # debug
    path = path + "login.csv"
    with open(path, "w") as file:
        file.write("username,password\n")


def game() -> None:
    choice = input_check("What do you want to do?", ["register", "login"])
    match choice:
        case "register":
            register()
        case "login":
            login(path)
        case _:
            print("Something went wrong!!!!!!!")


game()
#register()
#login(path)
#clear_login_file(path)
