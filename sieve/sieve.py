
def sieve(n):

    if n < 2:
        return []
    elif n == 2:
        return [2]

    sieve_list = [i for i in range(2, n + 1)]

    for number in sieve_list:
        checker = number

        for i in sieve_list:
            checker += number

            for j in sieve_list:

                if j == checker:
                    del sieve_list[sieve_list.index(j)]

    return sieve_list
