def solve(U, Y):

    # creat x matrix
    X = [[0] for i in range(len(U))]

    # calculate x matrix
    for i in range(len(U) - 1, -1, -1):
        sum = 0
        for j in range (len(U) - 1, i - 1, -1):
            sum = sum + U[i][j] * X[j][0]
        X[i][0] = (Y[i][0] - sum) / U[i][i]

    #return the calculated x matrix
    return (X)
