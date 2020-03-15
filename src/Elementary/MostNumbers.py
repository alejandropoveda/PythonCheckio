def checkio(*args):
    input_list = list(args)
    result = 0
    if len(input_list) > 0:
        min_element = max_element = input_list[0]
        for i in range(1, len(input_list)):
            current_element = input_list[i]
            if current_element < min_element:
                min_element = current_element
            elif current_element > max_element:
                max_element = current_element

        result = max_element - min_element

    return result


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def almost_equal(checked, correct, significant_digits):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision


    print('Example:')
    print(checkio(1, 2, 3))

    assert almost_equal(checkio(1, 2, 3), 2, 3), "3-1=2"
    assert almost_equal(checkio(5, -5), 10, 3), "5-(-5)=10"
    assert almost_equal(checkio(10.2, -2.2, 0, 1.1, 0.5), 12.4, 3), "10.2-(-2.2)=12.4"
    assert almost_equal(checkio(), 0, 3), "Empty"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
