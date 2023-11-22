n1 = int(input())
n2 = int(input())
resul = 0


while (n1 and n2) != 0:
    digit1 = n1 % 10
    resul = resul * 10 + digit1
    n1 //= 10

    digit1 = n2 % 10
    resul = resul * 10 + digit1
    n2 //= 10

print(resul)