def cycle_length(number, digits):

    check = set()
    check2 = set()
    a = number
    b = 1

    def next_middle_square(number, digits):
        k = digits // 2         # half of the number of digits
        square = number*number  # compute the square
        middle = (square // (10**k)) % (10**digits)   # extract middle part
        return middle
        
    while b>0:
        a = next_middle_square(a, digits)
        
        if a in check:
            break
        else:
            check.add(a)


    while b>0:
        a = next_middle_square(a, digits)
        
        if a in check2:
            break
        else:
            check2.add(a)
        
    resul = len(check2)
    

    return resul

print(cycle_length(1234,4))