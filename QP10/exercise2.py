import math

def comprehensions(i:int,j:int) -> tuple:
    n1 = list([x for x in range(i,j+1) if x % 10 == 3 or x % 10 == 8]) 
    n2 = tuple([round(math.sqrt(x),2) for x in range(i,j+1)])
    n3 = {num: chr(num) for num in range(i, j+1)}
    return n1, n2, n3

