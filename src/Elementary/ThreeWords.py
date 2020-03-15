def checkio(words: str) -> bool:
    accum = 0
    from re import findall
    word_list = findall(r'(\w+)', words)
    i = 0
    while i < len(word_list) and accum < 3:
        if word_list[i].isalpha():
            accum += 1
        else:
            accum = 0

        i += 1

    return accum == 3


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))

    assert checkio("one two 3 four five 6 seven eight 9 ten eleven 12") == False, "Hello"
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
