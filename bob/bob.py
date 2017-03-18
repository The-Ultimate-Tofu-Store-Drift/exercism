
def hey(what):

    # This replaces the '\t'. Yeah, I know.
    what = what.replace("\t", "")

    # This block is necessary for checking.
    special = [".", "!", "?", "%", "*", "^", "(", "@", "#", "$", "1", "2", "3", " ", ",", ""]
    numbers = ["1", "2", "3", "4"]
    empty = ["", " ", "    "]

    # This checks if the string contains characters from the variable 'empty'.
    if what[:] in empty:
        return "Fine. Be that way!"

    # It checks if the characters are not in 'special'. If so, it appends them to 'new_list'.
    new_list = []
    l = list(what)
    for i in l:
        if i not in special:
            new_list.append(i)

    # It just joins the content of 'new_list' to a string.
    new_list = "".join(new_list)

    # If the last character is ' ' it replaces all of them with ''.
    if what[-1] == " ":
        what = what.replace(" ", "")

    # This one checks if the character in 'new_list' are all uppercase-letters and are not in 'numbers'
    if new_list[:] == new_list[:].upper() and new_list[:] != "" and new_list not in numbers:
        return "Whoa, chill out!"

    # Checks if the last character is '?'.
    elif what[-1] == "?":
        return "Sure."

    else:
        return "Whatever."
