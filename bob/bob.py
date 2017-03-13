
def hey(what):

    what = what.replace("\t", "")
    special = [".", "!", "?", "%", "*", "^", "(", "@", "#", "$", "1", "2", "3", " ", ",", ""]
    numbers = "123"
    new_list = []

    n_what = what
    n_what = n_what.replace(",", "")
    n_what = n_what.replace(" ", "")

    for i in n_what:
        if i in n_what:
            n_what.replace(i, "")
            if len(n_what) == 0:
                return "Whatever."


    l = list(what)
    for i in l:
        if i not in special:
            new_list.append(i)

    new_list = "".join(new_list)

    print("what: ", what)
    print("new_list: ", new_list)
    print()

    if new_list[:] == new_list[:].upper() and new_list[:] != "":
        return "Whoa, chill out!"

print(hey('1, 2, 3'))

# 'ZOMG THE %^*@#$(*^ ZOMBIES ARE COMING!!11!!1!'
# 'ÜMLäÜTS!'
# 'Ending with ? means a question.'
# "Wait! Hang on. Are you going to be OK?"
# '    \t'
# '         hmmmmmmm...'
# 'What if we end with whitespace?   '
# 'This is a statement with trailing whitespace   '
# ''
# 4?
# '1, 2, 3'
# '1, 2, 3 GO!'
# 8 out of 8 m8
