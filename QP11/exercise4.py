def bisect(f, n):
    """Return the root of f(x) = 0 in the interval [a,b] by bisection."""
    a, b = 0, 1
    for i in range(n):
        x = (a + b) / 2
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x
    return round(x,5)

