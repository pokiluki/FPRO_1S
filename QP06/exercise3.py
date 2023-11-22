def change(amount):
    resul= []
    coins = [200,100,50,20,10,5,2,1]
    while amount != 0:
        for i in coins:
            d = amount//i
            amount = amount - d*i
            while d != 0:
                resul.append(i)
                d = d-1

    return resul
