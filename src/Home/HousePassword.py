def checkio(data: str) -> bool:

    from re import search

    pattern_digit = "[0-9]"
    pattern_upper_case = "[A-Z]"
    pattern_lower_case = "[a-z]"

    return len(data) >= 10 and \
        bool(search(pattern_digit, data)) and \
        bool(search(pattern_upper_case, data)) and \
        bool(search(pattern_lower_case, data))

# Some hints
# Just check all conditions


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
