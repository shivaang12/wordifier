import enchant


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


def find_vanity_number_format(phone_number: str):
    # TODO(shivaang12): To find some good regex to eliminate this code
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
