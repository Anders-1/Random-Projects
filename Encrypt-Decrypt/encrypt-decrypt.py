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
        decoded = letters[int(number)]
        # Join result.
        result = result + decoded

    return result

# encode("abcdefghijkl", 1)
# decode("010203040506070809101112", 1)

if encode("abcdefghijkl", 1) != "010203040506070809101112":

    print("ERROR WITH 'encode()'")
    print("010203040506070809101112 should be the result")

if decode("010203040506070809101112", 1) != "abcdefghijkl":

    print("ERROR WITH 'decode()'")
    print("abcdefghijkl should be the result")


# User input.
def getUserInput():

    # Variables
    encrypt_pattern = re.compile("[A-Za-z]+")
    decrypt_pattern = re.compile("^[0-9]+$")
    pattern = encrypt_pattern
    action = ""
    please_texts = {

        "a-z": "Please only use a-z.",
        "integers": "Please only use integers.",
        "e or d": "Please enter 'e' or 'd'."

    }
    please_text = ""

    # Encrypt or decrypt.
    valid = False
    please_text = "e or d"
    user_input = input("Would you like to (e)ncrypt or (d)ecrypt?\n")

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
            print(please_texts[please_text])
            user_input = input("Would you like to (e)ncrypt or (d)ecrypt?\n")

    # Set regex and please text.
    if action == "encrypt":
        pattern = encrypt_pattern
        please_text = "a-z"
    elif action == "decrypt":
        pattern = decrypt_pattern
        please_text = "integers"
    else:
        print("WARNING: Variable 'action' is not in range!" + action + " is what action is. \n")

    # What to encrypt/decrypt.
    valid = False
    text = input("What would you like to " + action + "?\n")

    while not valid:

        if pattern.fullmatch(text) == None or text == "\n":
            print(please_texts[please_text])
            text = input("What would you like to " + action + "?\n")
        else:
            valid = True
            print()

    # Key.
    valid = False
    please_text = "integers"
    pattern = decrypt_pattern
    key = input("What is your key?\n")

    while not valid:

        if pattern.fullmatch(key) == None or text == "\n":
            print(please_texts[please_text])
            key = input("What is your key?\n")
        else:
            valid = True
            print()

    # Function.
    if action == "encrypt":
        print(encode(text, key) + " is your encrypted text. \n")
        getUserInput()
    elif action == "decrypt":
        print(decode(text, key) + " is your decrypted text. \n")
        getUserInput()
    else:
        print("WARNING: Variable 'action' is not in range!" + action + " is what action is. \n")
        getUserInput()

getUserInput()
