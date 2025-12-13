import os
import hashlib

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
        print(message, "Choose ", end="")
    else:
        print(message + ",", "Choose ", end="")

    if len(choices) == 1:
        print(choices[0], end=": ")
    else:
        for choice in choices:
            if choice != choices[-1]:
                print(choice + ",", end=" ")
            else:
                print(choice, end=": ")


def clear_terminal() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def hash_it(string: str) -> str:
    to_hash = bytes(string, encoding="utf-8")
    return hashlib.sha256(to_hash).hexdigest()
