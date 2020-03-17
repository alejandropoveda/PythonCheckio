def get_format_time_in_minutes(t: str) -> int:
    hours, minutes = t.split(':')
    return (int(hours) * 60) + int(minutes)


def sun_angle(time)-> [int, str]:
    #replace this for solution
    ratio_angle_perminute: float = 0.25
    min_time_in_minutes_allowed = 6 * 60
    max_time_in_minutes_allowed = 18 * 60
    result = "I don't see the sun!"

    time_in_minutes = get_format_time_in_minutes(time)
    if min_time_in_minutes_allowed <= time_in_minutes <= max_time_in_minutes_allowed:
        result = (time_in_minutes - min_time_in_minutes_allowed) * ratio_angle_perminute

    return result

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")