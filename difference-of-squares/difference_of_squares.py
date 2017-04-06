
def square_of_sum(n):

    su = 0

    for i in range(n + 1):
        su += i

    su *= su
    return su


def sum_of_squares(n):

    su = 0

    for i in range(n + 1):
        su = su + (i * i)

    return su


def difference(n):
    return square_of_sum(n) - sum_of_squares(n)
