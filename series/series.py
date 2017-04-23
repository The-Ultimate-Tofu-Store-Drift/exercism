
def slices(string, digit):

    temp = []
    result = []

    if digit > len(string) or digit == 0:
        raise ValueError

    for i in range(len(string)):
        if len(string[i:i + digit]) == digit:
            temp.append(string[i:i + digit])

    for i in range(len(temp)):
        result.append([])

        for j in temp[i]:
            result[i].append(int(j))

    return result
