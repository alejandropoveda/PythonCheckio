def long_repeat(line: str) -> int:
    """
        length the longest substring that consists of the same char
    """
    # your code here
    result = 0
    i = 0
    line_len = len(line)
    while i < line_len:
        current_element = line[i]
        local_count = 0
        j = i
        while j < line_len and line[j] == current_element:
            local_count += 1
            j += 1

        if result < local_count:
            result = local_count

        i = j

    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')