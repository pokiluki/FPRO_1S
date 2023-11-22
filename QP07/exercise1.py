def switch_dict(adict):
    res = {}
    for m in adict:
        e = adict[m]
        if e in res:
            res[e].append(m)

        else:
            list = []
            list.append(m)
            res[e] = list
        

    return res
