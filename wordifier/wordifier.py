"""Main module."""


from . import helper


def number_to_words(number: str) -> str:
    return number


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

    for char_ind in range(len(wordify_number)):
        if wordify_number[char_ind].isalpha():
            for item in helper.number_to_alpha_dict.items():
                if wordify_number[char_ind] in item[1]:
                    wordify_number = wordify_number[:char_ind] + item[0] + \
                        wordify_number[char_ind+1:]

    wordify_number = wordify_number[:3] + "-" + wordify_number[3:]
    return prefix_number + wordify_number


def all_wordifications(number: str) -> list:
    return [number]
