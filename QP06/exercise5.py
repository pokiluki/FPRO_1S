def mult(M, N):
    # Check if the matrices have compatible dimensions for multiplication
    if len(M[0]) != len(N):
        return []

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(len(N[0]))] for _ in range(len(M))]

    # Perform matrix multiplication
    for i in range(len(M)):
        for j in range(len(N[0])):
            for k in range(len(N)):
                result[i][j] += M[i][k] * N[k][j]

    return result

