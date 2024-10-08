def biggest_member(atuple:tuple, sub:bool=False) -> tuple:
    arr = [(atuple, len(atuple))]

    for x in atuple:
        if type(x) == tuple: arr.append(biggest_member(x, sub=True))
    
    if sub: return sorted(arr, key=lambda x: x[1], reverse=True)[0]
    return sorted(arr, key=lambda x: x[1], reverse=True)[0][0]
        

print(biggest_member((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))