def magic(mat):
    n = len(mat)
    
    sumd1 = 0
    sumd2 = 0
    
    for i in range(n):
        sumd1 += mat[i][i]
        sumd2 += mat[i][n-i-1]

    if sumd1 != sumd2:
        return False
    
    for i in range(n):
        suml = 0
        sumc = 0

        for j in range(n):
            suml += mat[i][j]
            sumc += mat[j][i]
            
        if not (suml==sumc==sumd1):
            return False
    
    return True
    

