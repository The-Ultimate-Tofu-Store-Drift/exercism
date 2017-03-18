
def decode():
    pass


def encode(string):

    encoded = {}
    counter = 1
    container = []
    single = []

    # for i in range(len(string)):
    #     for j in range(len(string) - 1 - i):
    #         if string[j] == string[j + 1]:

    for i in string:
        if i in encoded:
            encoded[i] += 1
        else:
            encoded[i] = 1

    print("encoded:", encoded)

    for i in string:
        if i not in single:
            single.append(i)

    print("single: ", single)

    for i in single:
        container.append(str(encoded[i]) + i)

    print("container: ", container)

    new = "".join(container)
    print(new)


print(encode("AABBBCCCC"))
