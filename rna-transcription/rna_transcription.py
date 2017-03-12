
def to_rna(code):

    new_code = []
    old_code = [i for i in code]

    for letter in old_code:
        if letter != "G" and letter != "C" and letter != "T" and letter != "A":
            return ""

    for letter in old_code:
        if letter == "G":
            new_code.append("C")
        elif letter == "C":
            new_code.append("G")
        elif letter == "T":
            new_code.append("A")
        elif letter == "A":
            new_code.append("U")

    return "".join(new_code)
