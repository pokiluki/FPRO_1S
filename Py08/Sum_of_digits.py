def sum_digits_rec(n):
    if n < 10:
        return n
    return n%10 + sum_digits_rec(n//10)