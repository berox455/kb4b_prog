import csv
import random
import matplotlib.pyplot as plt
import os.path

path = "projekty/cichnaonar/"  # path to the project without a file
#path = "projekty/cichnaonar/quiz_questions.csv"
#
#with open(path, "r") as file:
#    reader = csv.DictReader(file)
#
#    for line in reader:
#        print(line)

def write_user(path: str) -> bool:
    if not os.path.isfile(path+"login.csv"):
        open(path + "login.csv", "w").close()
        return False
    else:
        name, password = create_user()
        print(f"name: {name}, password: {password}")
        if input("Is this information correct? [y][n]\t").lower() != "y":
            return False

        with open(path + "login.csv", "a") as file:
            file.write(f"{name}, {password}\n")
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


def clear_login_file() -> None:  # debug
    open(path + "login.csv", "w").close()


#register()
clear_login_file()
