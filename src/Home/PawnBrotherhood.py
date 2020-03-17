def gen_position(letter_in_ascii: int, number: int) -> str:
    return chr(letter_in_ascii) + str(number)


def gen_protectors_for_white_pawns(pawn: str):
    letter, number = pawn
    protectors = []
    number_int = int(number)
    if number_int > 1:
        protectors_number = number_int - 1
        letter_ascii = ord(letter)
        if letter_ascii > ord("a"):
            protectors.append(gen_position(letter_ascii - 1, protectors_number))
        if letter_ascii < ord("h"):
            protectors.append(gen_position(letter_ascii + 1, protectors_number))

    return protectors


def safe_pawns(pawns: set) -> int:
    safe_accum = 0
    for pawn in pawns:
        possible_protectors = gen_protectors_for_white_pawns(pawn)
        posible_protector_len = len(possible_protectors)
        i = 0
        while i < posible_protector_len:
            posible_protector = possible_protectors[i]
            if posible_protector in pawns:
                safe_accum += 1
                i = posible_protector_len
            i += 1

    return safe_accum


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))

    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")