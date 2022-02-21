def encode(string, key):

    string = string.lower()
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    result = []

    for letter in string:

        # Encode letters
        index = letters.index(letter)
        index = index + key

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

    #Dont need this 'print' any more.
    print(result)
    return result

def decode(string, key):

    string = string.lower()
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    result = ""
    string_list = []

    for index in range(0, len(string), 2):
        string_list.append(string[index : index + 2])

    for number in string_list:

        number = int(number) - key
        decoded = letters[int(number)]
        result = result + decoded
        result = ''.join(result)

    print(result)
    return result

# encode("abcdefghijkl", 1)
# decode("010203040506070809101112", 1)

if encode("abcdefghijkl", 1) != "010203040506070809101112":

    print("ERROR WITH 'encode()'")
    print("010203040506070809101112 should be the result")

if decode("010203040506070809101112", 1) != "abcdefghijkl":

    print("ERROR WITH 'encode()'")
    print("abcdefghijkl should be the result")
