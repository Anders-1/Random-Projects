def encode(string, key):

    string = string.lower()
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    result = []

    for letter in string:

        #Encode letters
        index = letters.index(letter)
        index = index + key
        letter = letters[index]

        #Reverse letters.
        i = 0
        result.insert(0, letter)
        ++i

    #Convert array to string.
    result = ''.join(result)
    print(result)


encode("AbC", 0)
