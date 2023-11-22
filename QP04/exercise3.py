def var_numbers(number, precision=2):

    soma = round(((number**2)+number)/2)
    
    mean = soma/number

    sums_up = 0
    for i in range(number):
        sums_up = sums_up + ((i-mean)**2)
    
    resul = round(((sums_up/number)-1), precision)

    return resul

