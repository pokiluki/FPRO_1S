def roman_to_integer(s):
    romans = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
    
    resul = 0 
    n = ""

    for w in s:
        if n == "":
            resul = resul + romans[w]
        elif romans[n]<romans[w] and n != "":
            resul = resul +romans[w]-2*romans[n]
        else:
            resul = resul + romans[w]
        n = w
    
    return resul

    