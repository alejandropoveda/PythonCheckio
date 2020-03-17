def build_ocurrences_dict(items: list):

    dict_of_ocurrencies = {}

    for key, value in [(element, 1) for element in items]:
        if key in dict_of_ocurrencies:
            dict_of_ocurrencies[key] = dict_of_ocurrencies[key] + value
        else:
            dict_of_ocurrencies[key] = value

    return dict_of_ocurrencies

def frequency_sort(items):
    # your code here
    dict_of_ocurrences = build_ocurrences_dict(items)
    list_of_ocurrences_sorted = sorted(dict_of_ocurrences.items(), key=lambda item: item[1], reverse=True)
    result = []
    for k, v in list_of_ocurrences_sorted:
        result += [k] * v

    return result


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
