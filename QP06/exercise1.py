def local_minima(alist):
    resul = []
    for i in range(len(alist)-2):
        jan = alist[i:(i+3)]
        minima = min(jan)
        if jan.count(minima) == 1:
            resul.append(minima)

    return resul

