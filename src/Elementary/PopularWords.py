def popular_words(text: str, words: list) -> dict:
    # your code here

    result = {element: 0 for element in words}
    from re import findall
    for word in findall(r'([\w\w\']+)', text):
        key = word.lower()
        if key in result:
            result[key] += 1

    return result


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")