
def abbreviate(phrase):

    temp = []
    acronym = []
    temporary_special = []
    special = [":", "-"]

    # replaces ':' and '-'
    for letter in phrase:
        if letter in special:
            phrase = phrase.replace(letter, " ")

    # makes a list
    phrase = phrase.split()

    # if a word consists entirely of uppercase letters, it will be replaced by the
    # first letter of this word
    for word in phrase:
        if word.isupper():
            temporary_special.append(word[0])
            del phrase[phrase.index(word)]
            phrase.insert(0, temporary_special[0])

    # joins the list to a string again
    phrase = " ".join(phrase)

    # inserts a empty space in front of every uppercase letter
    for letter in phrase:
        if letter.isupper():
            temp.append(" " + letter)
        else:
            temp.append(letter)

    # first joins the single letters to a string and then splits them to words
    temp = "".join(temp).split()

    # takes all the first letter of each word
    for word in range(len(temp)):
        acronym.append(temp[word][0])

    # returns and makes them to uppercase letters
    return "".join(acronym).upper()
