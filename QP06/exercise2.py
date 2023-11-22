def mastermind(guess, key):
    points1 = 0
    points2 = 0
    resul = ()

    
    for i in range(len(key)):
        if guess[i] == key[i]:
            points1 += 1
           
            guess[i] = key[i] = None

   
    for i in range(len(key)):
        if guess[i] is not None and guess[i] in key:
            points2 += 1
            
            key[key.index(guess[i])] = None

    resul = (points1, points2)

    return resul



