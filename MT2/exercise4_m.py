def add(num1i,num2i):
    num1 = num1i.split(".")
    num2 = num2i.split(".")
    while len(num1[0]) != len(num2[0]):
        if len(num1[0]) < len(num2[0]):
            num1[0] = "0" + num1[0]

        else:
            num2[0] = "0" + num2[0]

    while len(num1[1]) != len(num2[1]):
        if len(num1[1]) < len(num2[1]):
            num1[1] =num1[1] + "0"

        else:
            num2[1] =num2[1] + "0"

    num1 = num1[0]+num1[1]
    num2 = num2[0]+num2[1]

    resuli = dsum(num1,num2)
    resulu = resuli[0]
    num1 = num1i.split(".")
    num2 = num2i.split(".")
    if (len(str(int(num1[0]))) < len(str(int(num2[0])))) and resuli[1] == 0:
        resul = resulu[:len(str(int(num2[0])))] + "." + resulu[len(str(int(num2[0]))):]
    if (len(str(int(num1[0]))) < len(str(int(num2[0])))) and resuli[1] != 0:
        resul = resulu[:len(str(int(num2[0])))+1] + "." + resulu[len(str(int(num2[0])))+1:]

    if (len(str(int(num1[0]))) > len(str(int(num2[0])))) and resuli[1] == 0:
        resul = resulu[:len(str(int(num1[0])))] + "." + resulu[len(str(int(num1[0]))):]
    if (len(str(int(num1[0]))) > len(str(int(num2[0])))) and resuli[1] != 0:
        resul = resulu[:len(str(int(num1[0])))+1] + "." + resulu[len(str(int(num1[0])))+1:]
    


    return resul
    





def dsum(num1,num2):
    carry = 0
    resul = ""
    for i in range(-1,-len(num1),-1):
        a_i = int(num1[-i])
        b_i = int(num2[-i])
        result_i = str((a_i + b_i + carry) % 10)
        carry = (a_i + b_i + carry) // 10
        resul = resul + result_i
    if carry>0:
        resul = carry + resul
    out = (resul,carry)

    return out
    

#print(add('0123.40', '0.567'))
