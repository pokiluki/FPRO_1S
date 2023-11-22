def isomorphic(s1,s2):
    def one_way(as1,as2):
        resul = {}
        for i in range(len(as1)):
            k = as1[i:i+1]
            v = as2[i:i+1]
            resul[k]=v

        return resul
    
    u = one_way(s1,s2)
    u2 = one_way(s2,s1)

    if len(u) == len(u2):
        result = "'" + s1 + "'" + " and " + "'" + s2 + "'" + " are isomorphic"

    else:
        result = "'" + s1 + "'" + " and " + "'" + s2 + "'" + " are not isomorphic"

    return result
