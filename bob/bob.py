# This solution is from the user 'j2towers'

def hey(saidtobob):
    saidtobob = saidtobob.rstrip()

    if saidtobob.isupper():
        return "Whoa, chill out!"
    elif saidtobob.endswith("?"):
        return "Sure."
    elif saidtobob.isspace() or saidtobob == "":
        return "Fine. Be that way!"
    else:
        return "Whatever."