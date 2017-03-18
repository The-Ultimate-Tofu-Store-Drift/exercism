
def decode():
    pass


def encode(string):

    coding = {}
    container = []
    single_letters = []

    for i in string:
        if i in coding:
            coding[i] += 1
        else:
            coding[i] = 1

    print("coding:", coding)

    for i in string:
        if i not in single_letters:
            single_letters.append(i)

    print("single_letters: ", single_letters)

    for i in single_letters:
        container.append(str(coding[i]) + i)

    print("container: ", container)

    encoded_string = "".join(container)
    print(encoded_string)


print(encode("AABBBCCCC"))
