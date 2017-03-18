
def decode():
    pass


def encode(string):

    coding = {}
    container = []

    for i in string:
        if i in coding:
            coding[i] += 1
        else:
            for key, value in coding.items():
                if value == 1:
                    coding[key] = "!"
            for key, value in coding.items():
                container.append(str(value) + str(key))
            coding.clear()
            coding[i] = 1
    else:
        for key, value in coding.items():
            if value == 1:
                coding[key] = "!"
        for key, value in coding.items():
            container.append(str(value) + str(key))
        coding.clear()

    print("container: ", container)
    print("coding:", coding)

    encoded_string = "".join(container)
    encoded_string = encoded_string.replace("!", "")
    return encoded_string


print(encode("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"))
