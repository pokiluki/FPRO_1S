n = input("Input a 4 digit number:")
n = int(n)
d1 = int(n/1000) * 1000
d2 = int((n-d1)/100) * 100
d3 = int((n-d1-d2)/10) * 10
d4 = int(n-d1-d2-d3)


print(str(d1) + "\n" + str(d2) + "\n" + str(d3) + "\n" + str(d4))