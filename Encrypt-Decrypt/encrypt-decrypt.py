def encode(string, key):

    string = string.lower()
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    result = []

    for letter in string:

        # Encode letters
        index = letters.index(letter)
        index = index + key

        # Adding 0 to the start of index if it is less than 10.
        if index < 9:

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

    print(result)
    return result

encode("abcdefghijkl", 1)

if encode("abcdefghijkl", 1) != "01020304050607089101112":

    print("ERROR WITH 'encode()'")
    print("01020304050607089101112 should be the result")
