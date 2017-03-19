

def decode(string):

    numbers = []
    temp_dict = {}
    decoded_string = []

    if string == "":
        return ""

    for i in string:
        if i.isnumeric():
            numbers.append(int(i))
            if len(numbers) > 1:
                comb_string = int(str(numbers[0]) + str(numbers[1]))
                numbers.clear()
                numbers.append(comb_string)
        else:
            try:
                temp_dict[i] = numbers[0]
                numbers.clear()
                for key, value in temp_dict.items():
                    decoded_string.append(key * value)
                temp_dict.clear()
            except IndexError:
                temp_dict[i] = 1
                for key, value in temp_dict.items():
                    decoded_string.append(key * value)
                temp_dict.clear()

    decoded_string = "".join(decoded_string)
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
