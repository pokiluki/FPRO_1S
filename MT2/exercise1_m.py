def time_diff(t1,t2):
    t1a = t1[0]*60+t1[1]
    t2a = t2[0]*60+t2[1]
    dif = abs(t1a-t2a)
    hd = dif//60
    md = abs(dif-(hd*60))


    resul = (hd,md)    
    return resul

#print(time_diff((2, 50), (3, 10)))
