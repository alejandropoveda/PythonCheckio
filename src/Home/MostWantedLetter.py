def checkio(text: str) -> str:

    # replace this for solution
    text = ''.join(filter(str.isalpha, text)).lower()
    text_split_into_chars = [(element, 1) for element in text]

    dict_of_letters_with_ocurrencies = {}

    for key, value in text_split_into_chars:
        if key in dict_of_letters_with_ocurrencies:
            dict_of_letters_with_ocurrencies[key] = dict_of_letters_with_ocurrencies[key] + value
        else:
            dict_of_letters_with_ocurrencies[key] = value

    def get_most_wanted(left_e: (str, int), right_e: (str, int)) -> (str, int):
        gmw_result = left_e
        if left_e[1] == right_e[1]:
            if right_e[0] < left_e[0]:
                gmw_result = right_e
        elif right_e[1] > left_e[1]:
            gmw_result = right_e

        return gmw_result

    list_of_letters_with_ocurrencies = [[k, v] for k, v in dict_of_letters_with_ocurrencies.items()]

    from functools import reduce
    result_letter: str = reduce(lambda a, b: get_most_wanted(a, b), list_of_letters_with_ocurrencies)[0]

    return result_letter


if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")