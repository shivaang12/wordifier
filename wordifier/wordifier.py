"""Main module."""


from . import helper
import itertools


def number_to_words(number: str) -> str:
    """
    Args:
    - number: A string representing US vanity phone number.
              e.g. "+1-800-724-6837", "1-800-724-6837", "8007246837"

    Returns:
    - str: a string which contains pain digit number.
              e.g. "1-800-PAINTER", "800-PAINTER"

              currently this function does not support return format
              such as 800PAINTER. Whatever format you provide in input
              it will return in "XXX-XXX-XXXX" or "1-XXX-XXX-XXXX" format.
    """
    possible_word_list = set()

    formated_number = helper.find_vanity_number_format(number)

    if formated_number == "":
        print("Invalid Number")
        return formated_number

    prefix_number, wordify_number = formated_number

    possible_indexes = helper.index_division_array.get_all_possible_indexes()

    # TODO(shivaang12): Should I use while loop?
    for element in possible_indexes:
        current_possible_list = [helper.find_words(wordify_number[sub_ele[0]: sub_ele[1]])
                                 for sub_ele in element]
        word_string_array = [(''.join(x)) for x in itertools.product(*current_possible_list)]

        for word in word_string_array:
            possible_word_list.add(word)

        if possible_word_list:
            # break when find some possible words
            break

    # Current algorithm allows to generate all digits (this is side effect for supporting
    # substring combination). We will remove every pure digit string
    possible_word_list = [x for x in possible_word_list if not x.isdigit()]

    # Sorting the set in terms of more alpha char count so that we get more quality content
    # in the beginning of the set.
    possible_word_list = sorted(possible_word_list, key=helper.count_alpha, reverse=True)

    # Now the following operation will format the sting if there is valid substring
    # for e.g. 72HOT37 => 72-HOT-37 and 7HONDA1 => 7HONDA1 (No change as 1 numeric char only)
    possible_word_list = [helper.get_alpha_numeric_format(x) for x in possible_word_list]

    # Append the prefix
    return prefix_number+possible_word_list[0]


def words_to_number(number: str) -> str:
    """
    Args:
    - number: A string representing US vanity phone number.
              e.g. "+1-800-PAINTER", "800-PAINT-37", "80072HOT37"

    Returns:
    - str: a string which contains pain digit number.
              e.g. "1-800-724-6837", "800-724-6837"

              currently this function does not support return format
              such as 8007246837. Whatever format you provide in input
              it will return in "XXX-XXX-XXXX" or "1-XXX-XXX-XXXX" format.
    """
    formated_number = helper.find_vanity_number_format(number)

    if formated_number == "":
        print("Invalid Number")
        return formated_number

    prefix_number, wordify_number = formated_number

    for char_ind, char in enumerate(wordify_number):
        if char.isalpha():
            for item in helper.number_to_alpha_dict.items():
                if char in item[1]:
                    wordify_number = wordify_number[:char_ind] + item[0] + \
                        wordify_number[char_ind+1:]

    wordify_number = wordify_number[:3] + "-" + wordify_number[3:]
    return prefix_number + wordify_number


def all_wordifications(number: str) -> list:
    return [number]
