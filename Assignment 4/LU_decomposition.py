def solve(A):
    n = len(A)

    #perform LU Decomposition
    #Both Upper and Lower triangular matrix will be stored on A matrix together
    for j in range(n):

        # upper trianguar matrix
        for i in range(j+1):
            sum = 0
            for k in range(i):
                sum = sum + A[i][k] * A[k][j]
            #store to A matrix
            A[i][j] = A[i][j] - sum

        #lower triangular matrix
        for i in range(j+1, n):
            sum = 0
            for k in range(j):
                sum = sum + A[i][k] * A[k][j]
            # store to M matrix
            A[i][j] = (A[i][j] - sum)/A[j][j]


    #print Lower triangual matrix from A matrix
    print("\nLower Triangular Matrix is = ")
    for i in range(n):
        for j in range(len(A[i])):
            if j > i:
                print("0.0", end='  ')
            elif j == i:
                print("1.0", end='  ')
            else:
                print(A[i][j], end='  ')
        print()

    #print Upper triangular matrix from A matrix
    print("\nUpper Triangular Matrix is = ")
    for i in range(n):
        for j in range(len(A[i])):
            if j < i:
                print("0.0", end='  ')
            else:
                print(A[i][j], end='  ')
        print()

    return (A)

