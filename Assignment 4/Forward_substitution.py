def solve(L, B):

    #creat Y matrix
    Y = [[0] for i in range(len(L))]

    # calculate Y matrix
    for i in range(len(L)):
        sum = 0
        for j in range (i+1):
            if i == j:
                pass
            else:
                sum = sum + L[i][j] * Y[j][0]
        Y[i][0] = (B[i][0] - sum)

    #return the calculated Y matrix
    return (Y)
