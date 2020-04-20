import itertools
import re
import enchant
from . import indexifier


# Dictionary object for checking word in english
english_dict = enchant.Dict("en_US")

# Map for number(Digit) to corresponding alphabets
number_to_alpha_dict = {
    "1": [],
    "2": ["A", "B", "C"],
    "3": ["D", "E", "F"],
    "4": ["G", "H", "I"],
    "5": ["J", "K", "L"],
    "6": ["M", "N", "O"],
    "7": ["P", "Q", "R", "S"],
    "8": ["T", "U", "V"],
    "9": ["W", "X", "Y", "Z"],
    "0": []
}


# Indexifier object for the array of substring possiblity combination
index_division_array = indexifier.Indexifier(7)


def find_vanity_number_format(phone_number: str):
    # TODO(shivaang12): To find some good regex to eliminate next 5 lines of this code
    phone_number = phone_number.replace('+', '')
    phone_number = phone_number.replace(' ', '')
    phone_number = phone_number.replace('(', '')
    phone_number = phone_number.replace(')', '')
    phone_number = phone_number.replace('-', '')

    if len(phone_number) > 9 and len(phone_number) <= 11:
        prefix = phone_number[:len(phone_number)-7]
        if len(prefix) > 3:
            prefix = prefix[:1] + "-" + prefix[1:]
        return prefix+"-", phone_number[len(phone_number)-7:]
    else:
        return ""


def find_words(number: str):
    # We want it to return number if no valid word combination is found
    # this will allowed to incorporate substring feature like
    # 72-HOT-37
    valid_words = [number]
    word_combination_array = list(itertools.product(*[number_to_alpha_dict[i] for i in number]))
    word_string_array = [(''.join(x)) for x in word_combination_array]

    for word in word_string_array:
        if len(word) == 1:
            # Currently pyenchant returns true for all alphabets and I
            # think only A and I would make a valid english one letter word
            if (word == "A" or word == "I"):
                valid_words.append(word)
        elif english_dict.check(word):
            valid_words.append(word)

    return valid_words


def count_alpha(number: str):
    count = 0
    for char in number:
        if char.isalpha():
            count += 1
    return count


def get_alpha_numeric_format(number: str):
    # This method will format the substring type possibilities
    # for e.g. 78HOT37 => 78-HOT-37
    # TODO(shivaang12): May be some room for improvement here.
    split_str = re.split(r'(\d+)', number)
    return_str = []
    for x in range(len(split_str)-1):
        if len(split_str[x]) > 1 and len(split_str[x+1]) > 1:
            return_str.append("-")
        else:
            return_str.append("")
            pass
    array = [j for i in zip(split_str, return_str) for j in i] + [split_str[-1]]
    return "".join(x for x in array)
