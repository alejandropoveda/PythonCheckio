def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    # your code here
    def isAllowed(c: str) -> bool:
        characters_not_allowed = re.compile("[.,\s]")
        return not bool(characters_not_allowed.match(c))

    result = ""
    import re
    text_trimed = text.strip()

    text_length = len(text_trimed)
    if text_length > 0:
        i = 0

        while i < text_length and not isAllowed(text_trimed[i]):
            i += 1

        index_first_character_of_first_word = i
        if text_length - 1 != index_first_character_of_first_word or isAllowed(text_trimed[index_first_character_of_first_word]):
            text_trimed = text_trimed[index_first_character_of_first_word:]
            j = 0
            while j < len(text_trimed) and isAllowed(text_trimed[j]):
                j += 1

            index_last_character_of_first_word = j

            result = text_trimed[:index_last_character_of_first_word]

    return result


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")