import random
import string


def generate_password(char_list, min_char_count, max_char_count):
    generated_password = ""

    password_len = random.choice(range(int(min_char_count), int(max_char_count)+1))

    for i in range(password_len):
        generated_password = generated_password + random.choice(char_list)

    return generated_password


def create_list(given_mode1, given_mode2, given_mode3, given_mode4, given_min_char, given_max_char):
    char_list = []
    punctuation_added = False
    upper_case_added = False
    lower_case_added = False
    numbers_added = False
    if given_mode1 == "1" and not punctuation_added:
        char_list = char_list + list(string.punctuation)
        punctuation_added = True
    if given_mode2 == "1" and not upper_case_added:
        char_list = char_list + list(string.ascii_uppercase)
        upper_case_added = True
    if given_mode3 == "1" and not lower_case_added:
        char_list = char_list + list(string.ascii_lowercase)
        lower_case_added = True
    if given_mode4 == "1" and not numbers_added:
        char_list = char_list + list(string.digits)
        numbers_added = True

    random.shuffle(char_list)

    generated_password = generate_password(char_list, given_min_char, given_max_char)
    return generated_password







