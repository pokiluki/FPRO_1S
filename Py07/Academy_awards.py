def academy_awards(alist):
    resul = {}
    for i in alist:
        if i[1] not in resul:
            resul[i[1]] = 1
        else:
            resul[i[1]] += 1
    return resul