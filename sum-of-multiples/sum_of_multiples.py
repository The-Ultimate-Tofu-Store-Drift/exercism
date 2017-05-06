
def sum_of_multiples(n, particular_numbers):

    range_of_numbers = [i for i in range(0, n)]
    result = []

    for number in particular_numbers:
        for range_number in range_of_numbers:

            if range_number % number == 0 and range_number not in result:
                result.append(range_number)

    result = sum(result)

    return result
