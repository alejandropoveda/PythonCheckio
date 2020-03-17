from typing import List


def check_triplets(line: str) -> str:
    result = line[0]
    if result != ".":
        accum = 1
        i = 1
        while i < len(line) and line[i] == result:
            accum += 1
            i += 1

        if accum != len(line):
            result = "."

    return result


def gen_column(board: List[str], column: int) -> str:
    result = ""
    i = 0
    while i < len(board):
        result += board[i][column]
        i += 1

    return result


def gen_diagonal(board: List[str], modifier: int) -> str:
    diagonal = ""
    i = 0
    while i < len(board):
        diagonal += board[i][abs(modifier - i)]
        i += 1

    return diagonal


def check_diagonals(board: List[str]) -> list:
    result = []
    diagonal_regular = gen_diagonal(board, 0)
    diagonal_reverse = gen_diagonal(board, 2)
    result.append(check_triplets(diagonal_regular))
    result.append(check_triplets(diagonal_reverse))

    return result


def gen_result(all_results: list, result: str) -> str:
    if len(all_results) == 0:
        return result
    else:
        head = all_results[0]
        tail = all_results[1:]
        if head != ".":
            return head
        else:
            return gen_result(tail, result)


def checkio(game_result: List[str]) -> str:

    i = 0
    all_results = []

    while i < len(game_result):
        all_results.append(check_triplets(game_result[i]))
        all_results.append(check_triplets(gen_column(game_result, i)))

        i += 1

    all_results += check_diagonals(game_result)

    result = gen_result(all_results, "D")

    return result


if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")