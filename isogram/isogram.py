# This is the solution from the user 'j2towers'

def is_isogram(phrase):
    for i in phrase.lower():
        if phrase.lower().count(i) > 1 and phrase.isalpha():
            return False
    return True
