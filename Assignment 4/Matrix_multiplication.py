def solve(A, B):
    n= len(A)
    AB =  [[0.0 for j in range(n)] for i in range(n)]
    for i in range(len(A)):
        for j in range(len(B[i])):
            add = 0
            for k in range(len(A[i])):
                multiply = (A[i][k] * B[k][j])
                add = add + multiply
            AB[i][j] = add
    return (AB)