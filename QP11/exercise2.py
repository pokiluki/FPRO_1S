def find_me(f, limits):
    lower_limit, upper_limit = limits
    iterations = 0

    while lower_limit <= upper_limit:
        mid = (lower_limit + upper_limit) // 2
        result = f(mid)

        iterations += 1

        if result == 0:
            return iterations
        elif result == -1:
            upper_limit = mid - 1
        else:
            lower_limit = mid + 1

    return None 


