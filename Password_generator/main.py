import random
import string

min_length = int(input("enter the desired password length:"))
has_number = input("do you want to have numbers? (y/n) ").lower() == "y"
has_special = input("do you want to have special characters? (y/n) ").lower() == "y"


def generate_password(length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    password = ""
    meets_criteria = False
    contains_number = False
    contains_special = False

    while not meets_criteria or len(password) < length:
        new_char = random.choice(characters)
        password += new_char

        if new_char in digits:
            contains_number = True
        elif new_char in special:
            contains_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = contains_number
        if special_characters:
            meets_criteria = meets_criteria and contains_special
    return password


pwd = generate_password(min_length, has_number, has_special)
print("Your new password is: " + pwd)
