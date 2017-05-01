
def encode(string_input):

    plain_key = "abcdefghijklmnopqrstuvwxyz"
    cipher_key = plain_key[::-1]

    temp = []

    for i in range(len(string_input)):

        if string_input[i].lower().isalpha():
            temp.append(cipher_key[plain_key.index(string_input[i].lower())])

        elif string_input[i].isnumeric():
            temp.append(string_input[i])

    output = []
    counter = 0

    for i in range(len(temp)):

        output.append(temp[i])
        counter += 1

        if counter == 5:

            if i + 1 != len(temp):
                output.append(" ")

            counter = 0

    return "".join(output)


def decode(string_input):

    plain_key = "abcdefghijklmnopqrstuvwxyz"
    cipher_key = plain_key[::-1]

    temp = []

    for i in range(len(string_input)):

        if string_input[i].isalpha():
            temp.append(plain_key[cipher_key.index(string_input[i])])

        elif string_input[i].isnumeric():
            temp.append(string_input[i])

    return "".join(temp)

if __name__ == "__main__":
    print(decode(input("string: ")))
