import math


def function(n: int, k: int):
    return (((2*n)/k) - k + 1) / 2


def f(n: int) -> list:

    result = []
    k = 1
    end_odds = False
    end_evens = False

    while not end_odds and not end_evens:

        if (k % 2 == 0 and n % (k/2) == 0) or (k % 2 != 0 and n % k == 0):
            a = function(n, k)
            if a % 1 == 0 and a > 0:
                a = int(a)
                result.append(list(range(a, a + k)))

            companion = n / k
            if companion % 1 == 0:
                a = function(n, int(companion))
                if a % 1 == 0 and a > 0:
                    a = int(a)
                    result.append(list(range(a, a + k)))

        k += 1
        if k % 2 == 0 and k > 2 * math.sqrt(n):
            end_evens = True
        elif k > math.sqrt(n):
            end_odds = True

    return result


if __name__ == '__main__':
    print(f(42))