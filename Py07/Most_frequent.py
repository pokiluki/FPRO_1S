def most_frequent(alist):
    resul = {}
    for i in alist:
        if i not in resul:
            resul[i] = 1
        else:
            resul[i] += 1
    
    max = 0
    for i in resul:
        if resul[i] > max:
            max = resul[i]
            res = i
        if resul[i] == max:
            if i > res:
                res = i
    return res