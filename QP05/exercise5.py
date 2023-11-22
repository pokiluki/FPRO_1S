def triplet(tup):
    for i in range(len(tup) - 2):
        a = tup[i]

        for j in range(i + 1, len(tup) - 1):
            b = tup[j]

            for k in range(j + 1, len(tup)):
                c = tup[k]

                if a + b + c == 0:
                    return (a, b, c)

    return ()



