import re

def encode(string, key):

    string = string.lower()
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    result = []

    for letter in string:

        # Encode letters
        index = letters.index(letter)
        index = index + int(key)

        # Adding 0 to the start of index if it is less than 10.
        if index <= 9:

            index = "0" + str(index)

        # Reverse letters.
        # i = 0
        # result.insert(0, index)
        # ++i

        result.append(index)

    # Convert int list to string list.
    result = [str(x) for x in result]
    # Convert string list to string.
    result = ''.join(result)

    return result

def decode(string, key):

    string = string.lower()
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    result = ""
    string_list = []

    # Chunk string into 2 letter segments in list.
    for index in range(0, len(string), 2):
        string_list.append(string[index : index + 2])

    for number in string_list:

        # Decode letter.
        number = int(number) - int(key)
        # COMBAK: FIX ERROR WITH NUMBER OUT OF LIST RANGE
        # print(str(number) + " IS THE NUMBER")
        decoded = letters[int(number)]
        # Join result.
        result = result + decoded

    return result

# REMEMBER TO UPDATE THIS WHEN CHANING THE ENCRYPTION/DECRYPTION ALGORYTHM!!!

if encode("abcdefghijkl", 1) != "010203040506070809101112":

    print("ERROR WITH 'encode()'")
    print("010203040506070809101112 should be the result")

if decode("010203040506070809101112", 1) != "abcdefghijkl":

    print("ERROR WITH 'decode()'")
    print("abcdefghijkl should be the result")


# User input.
asked_color = False

def getUserInput():

    # Variables
    encrypt_pattern = re.compile("[A-Za-z]+")
    decrypt_pattern = re.compile("^[0-9]+$")
    pattern = encrypt_pattern
    action = ""
    color = False
    class colors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKCYAN = '\033[96m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

    please_texts = {

        "a-z": colors.UNDERLINE + "Please only use a-z." + colors.ENDC,
        "integers": colors.UNDERLINE + "Please only use integers." + colors.ENDC,
        "e or d": colors.UNDERLINE + "Please enter 'e' or 'd'." + colors.ENDC,
        "y or n": "Please enter 'y' or 'n'."

    }
    global asked_color

    # Color
    if not asked_color:

        valid = False
        please_text = "y or n"
        user_input = input("Would like to use color (y) or not (n)? \n")

        while not valid:

            if user_input == "y":
                color = True
                valid = True
                asked_color = True
                print()
            elif user_input == "n":
                color = False
                valid = True
                asked_color = True
                print()
            else:
                print()
                print(please_texts[please_text])
                user_input = input("Would like to use color (y) or not (n)? \n")

    # Color class setting

    if color:

        class colors:
            HEADER = '\033[95m'
            OKBLUE = '\033[94m'
            OKCYAN = '\033[96m'
            OKGREEN = '\033[92m'
            WARNING = '\033[93m'
            FAIL = '\033[91m'
            ENDC = '\033[0m'
            BOLD = '\033[1m'
            UNDERLINE = '\033[4m'

    elif not color:

        class colors:
            HEADER = ''
            OKBLUE = ''
            OKCYAN = ''
            OKGREEN = ''
            WARNING = ''
            FAIL = ''
            ENDC = ''
            BOLD = ''
            UNDERLINE = ''

    else:

        print("WARNING: Variable 'color' is not in range! " + color + " is what action is. \n")

    # Encrypt or decrypt.
    valid = False
    please_text = "e or d"
    user_input = input(colors.OKCYAN + "Would you like to (e)ncrypt or (d)ecrypt? \n" + colors.ENDC)

    while not valid:

        if user_input == "e":
            action = "encrypt"
            valid = True
            print()
        elif user_input == "d":
            action = "decrypt"
            valid = True
            print()
        else:
            print()
            print(please_texts[please_text])
            user_input = input(colors.OKCYAN + "Would you like to (e)ncrypt or (d)ecrypt? \n" + colors.ENDC)

    # Set regex and please text.
    if action == "encrypt":
        pattern = encrypt_pattern
        please_text = "a-z"
    elif action == "decrypt":
        pattern = decrypt_pattern
        please_text = "integers"
    else:
        print(colors.WARNING + "WARNING: Variable 'action' is not in range! " + action + " is what action is. \n" + colors.ENDC)

    # What to encrypt/decrypt.
    valid = False
    text = input(colors.OKCYAN + "What would you like to " + action + "? \n")

    while not valid:

        if pattern.fullmatch(text) == None or text == "\n":
            print()
            print(please_texts[please_text])
            text = input(colors.OKCYAN + "What would you like to " + action + "? \n" + colors.ENDC)
        else:
            valid = True
            print()

    # Key.
    valid = False
    please_text = "integers"
    pattern = decrypt_pattern
    key = input(colors.OKCYAN + "What is your key? \n" + colors.ENDC)

    while not valid:

        if pattern.fullmatch(key) == None or text == "\n":
            print()
            print(please_texts[please_text])
            key = input(colors.OKCYAN + "What is your key? \n" + colors.ENDC)
        else:
            valid = True
            print()

    # Function.
    if action == "encrypt":
        print(colors.OKCYAN + encode(text, key) + " is your encrypted text. \n" + colors.ENDC)
        getUserInput()
    elif action == "decrypt":
        print(colors.OKCYAN + decode(text, key) + " is your decrypted text. \n" + colors.ENDC)
        getUserInput()
    else:
        print(colors.WARNING + "WARNING: Variable 'action' is not in range! " + action + " is what action is. \n" + colors.ENDC)
        getUserInput()

getUserInput()
