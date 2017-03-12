# coding=utf-8


def word_count(string):
    """Well, at least it works."""

    string_list = string.replace("\n", " ")
    string_list = string_list.replace("\t", " ")
    string_list = string_list.replace("_", " ")
    string_list = string_list.replace(",", " ")
    string_list = string_list.replace(".", " ")
    string_list = string_list.replace("🖖", " ")
    string_list = list(string_list)

    special = [":", "!", "&", "@", "$", "^", "%"]
    new_string_list = []

    for i in string_list:
        if i not in special:
            new_string_list.append(i)

    print(new_string_list)

    new_string = "".join(new_string_list)
    new_string = new_string.lower()
    print(new_string)
    new_string = new_string.split(" ")

    new_string_1 = []

    for i in new_string:
        if i != "":
            new_string_1.append(i)

    print(new_string_1)

    counter = {}

    for i in new_string_1:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1

    return counter
