
def is_pangram(word_or_sentence):

    string = word_or_sentence.lower()

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alpha = [i for i in alphabet]

    for letter in string:
        if letter in alpha:
            alpha.remove(letter)
        else:
            pass

    if len(alpha) > 0:
        return False
    else:
        return True
