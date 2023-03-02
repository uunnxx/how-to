def format_duration(seconds):
    # res = [seconds // 60, seconds // 24, seconds // 365]
    minute = 60
    hour = minute * 60
    day = hour * 24
    year = day * 365
    res = divmod(seconds, year)
    res2 = divmod(seconds, day)
    res3 = divmod(seconds, hour)
    res4 = divmod(seconds, minute)
    # res = [, seconds // day, seconds // hour, seconds // minute]
    print(res)
    print(res2)
    print(res3)
    print(res4)


# format_duration(1)
format_duration(65)
format_duration(3600)
