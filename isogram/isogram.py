
def is_isogram(phrase):

    phrase = phrase.lower()
    phrase = phrase.replace(" ", "")
    phrase = phrase.replace("-", "")

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet = list(alphabet)

    temp = []

    for i in phrase:
        if i in alphabet:
            temp.append(i)
            del alphabet[alphabet.index(i)]

        elif i not in alphabet:
            return False

    if "".join(temp) == phrase:
        return True
