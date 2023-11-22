def mastermind(g1, g2, g3, c1, c2, c3):
    guess = [g1, g2, g3]
    key = [c1, c2, c3]
    points = 0

    
    for i in range(3):
        if guess[i] == key[i]:
            points += 3
           
            guess[i] = key[i] = None

   
    for i in range(3):
        if guess[i] is not None and guess[i] in key:
            points += 1
            
            key[key.index(guess[i])] = None

    return points


