import math


def function(n: int, k: int):
    return (((2 * n) / k) - k + 1) / 2


#
# This is not neccesary but i wanted to check how to build all the series.
#
def gen_consecutive_positives_series(n: int) -> list:

    already_checked = []
    result = []
    k = 1
    end_odds = False
    end_evens = False

    def macro_check_conditions_for_this_iteration() -> bool:
        result_check_conditions = False
        if k % 2 == 0:
            if not end_evens and n % (k / 2) == 0:
                result_check_conditions = True

        else:
            if not end_odds and n % k == 0:
                result_check_conditions = True

        return result_check_conditions

    while not end_odds or not end_evens:

        if k % 2 == 0 and k > 2 * math.sqrt(n):
            end_evens = True
        elif k % 2 != 0 and k > math.sqrt(n):
            end_odds = True

        if macro_check_conditions_for_this_iteration():
            a = function(n, k)
            if a % 1 == 0 and a > 0:
                a = int(a)
                result.append(list(range(a, a + k)))
                already_checked.append(k)

            companion = n / k
            if companion % 1 == 0 and not(int(companion) in already_checked):
                companion = int(companion)
                a = function(n, int(companion))
                if a % 1 == 0 and a > 0:
                    a = int(a)
                    result.append(list(range(a, a + companion)))

        k += 1

    return result


def count_consecutive_summers(num):
    # your code here

    result = [[1]]
    if num != 1:
        result = gen_consecutive_positives_series(num)

    return len(result)


if __name__ == '__main__':
    print("Example:")
    print(count_consecutive_summers(15))
    print(count_consecutive_summers(42))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_consecutive_summers(42) == 4
    assert count_consecutive_summers(99) == 6
    assert count_consecutive_summers(1) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")


