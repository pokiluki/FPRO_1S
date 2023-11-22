def next_prime(n):
    while True:
        n +=1
        counter = 0
        for i in range(2,n):
            if n%i == 0:
                counter += 1
                break
        if counter == 0:
            return n

#print(next_prime(26))

