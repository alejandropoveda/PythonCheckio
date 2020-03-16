from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    # your code here
    are_the_same = True
    elements_len = len(elements)
    if elements_len > 0:
        element = elements[0]
        i = 1
        while i < elements_len and are_the_same:
            if elements[i] != element:
                are_the_same = False
            i += 1

    return are_the_same


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")