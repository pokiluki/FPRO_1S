def sparse_dot_product(d1,d2):
    resul = 0
    
    for i in d1:
        if i in d2:
            resul = resul + (d1[i]*d2[i])

    return resul


