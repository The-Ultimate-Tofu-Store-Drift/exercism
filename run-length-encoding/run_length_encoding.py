

def decode(string):

    # for storing data
    numbers = []
    temp_dict = {}
    decoded_string = []

    # simply returns 'nothing' if the given argument is 'nothing'.
    if string == "":
        return ""

    for i in string:

        if i.isnumeric():           # if i is a number
            numbers.append(int(i))  # it will be converted to a 'int' and stored in 'numbers'

            # if two numbers appear in a row, they will be merged and stored in 'numbers'
            # it is necessary in case something is given like this: 12W24B
            if len(numbers) > 1:
                comb_string = int(str(numbers[0]) + str(numbers[1]))
                numbers.clear()
                numbers.append(comb_string)

        else:
            # Tries to combine 'i' and the int stored in 'numbers'
            # Afterwards all entry in 'numbers' will be removed
            try:
                temp_dict[i] = numbers[0]
                numbers.clear()

                # This is an important step because otherwise the key/value pairs will be overwritten by
                # the same letter e.g. 2AB3A != dict= {'A' : 2, 'B' : 1, 'A' : 3}; It's dict= {'A' : 3, 'B' : 1}
                # In the dictionary is always only one key/value and will be added the list 'decoded_string'.
                for key, value in temp_dict.items():
                    decoded_string.append(key * value)  # e.g. {'A' : 3} > AAA

                temp_dict.clear()   # removes all entries

            # If a letter is followed by another letter, there is no value for the key in 'number'
            # therefore a 'IndexError' is raised. The value '1' is given to the key.
            except IndexError:
                temp_dict[i] = 1

                for key, value in temp_dict.items():
                    decoded_string.append(key * value)

                temp_dict.clear()

    decoded_string = "".join(decoded_string)    # 'decoded_string' is a list. But we need a string
    return decoded_string


def encode(string):
    # One dictionary called 'coding' to temporally store the count of letters
    # and a the list 'container' to store the strings.
    coding = {}
    container = []

    # Checks if the letter is already in the dictionary. If so it increases the key by one.
    for i in string:
        if i in coding:
            coding[i] += 1
        else:

            # If the value for a key is '1', the value will be changed to '!'.
            # This makes is possible to get rid of them by replacing them with ''.
            # It changes the dictionary. This is important to know.
            for key, value in coding.items():
                if value == 1:
                    coding[key] = "!"

            # It takes the key and value and transforms them in strings.
            # After that combines both and appends the string in the 'container'.
            for key, value in coding.items():
                container.append(str(value) + str(key))
            coding.clear()  # Deletes everything in the dictionary
            coding[i] = 1   # Creates a new entry for the letter
    # When the for-loop is done, there is still a entry in 'coding' left.
    # This 'else' block does exactly the same thing like the 'for' block before but it transfers the last entry.
    else:

        for key, value in coding.items():
            if value == 1:
                coding[key] = "!"

        for key, value in coding.items():
            container.append(str(value) + str(key))
        coding.clear()

    encoded_string = "".join(container)                 # makes a string out of the list 'container'
    encoded_string = encoded_string.replace("!", "")    # replaces all '!' with ''

    return encoded_string
