#
# Skeleton file for the Python "Hello World" exercise.
#


def hello(name=''):

    if name == '':
        return "Hello, World!"
    elif name == None:
        return "Hello, World!"
    else:
        return "Hello, %s!" % name
