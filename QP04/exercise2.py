def adigits(a, b, c):
    a_str = str(a)
    b_str = str(b)
    c_str = str(c)

    list = [a_str, b_str, c_str]

    list.sort()

    resul = int("".join(list))

    return resul

