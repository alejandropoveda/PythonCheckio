def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    if len(array) == 0:
        result = 0
    else:
        def sumOnlyTheEvenElementsInAnArray(arr):
            accum = 0
            for i in range(0, len(arr), 2):
                accum += arr[i]

            return accum

        result_of_sum_the_even_elements = sumOnlyTheEvenElementsInAnArray(array)
        result = result_of_sum_the_even_elements * array[-1]

    return result


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio([0, 1, 2, 3, 4, 5]))

    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")