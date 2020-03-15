def best_stock(a) -> str:
    # your code here
    index_key = 0
    index_value = 1
    list_of_items = list(a.items())
    result = ()
    for i in range(0, len(a)):
        if i == 0:
            result = list_of_items[i]
        else:
            current_element = list_of_items[i]
            if current_element[index_value] > result[index_value]:
                result = current_element

    return result[index_key]


if __name__ == '__main__':
    print("Example:")
    print(best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}) == "ATX"
    assert best_stock({"CAC": 91.1, "ATX": 1.01, "TASI": 120.9}) == "TASI"
    print("Coding complete? Click 'Check' to earn cool rewards!")
