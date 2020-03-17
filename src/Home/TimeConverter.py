def time_converter(time):
    #replace this for solution
    am = " a.m."
    pm = " p.m."

    hours_str, minutes_str = time.split(':')
    hours_int: int = int(hours_str)
    noon: int = 12
    period = am
    if hours_int == 0:
        hours_int = 12
    elif hours_int >= 12:
        if hours_int > 12:
            hours_int -= 12
        period = pm

    return str(hours_int) + ':' + minutes_str + period


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")