import Partial_pivot
def solve(A):
    #row loop
    for r1 in range(len(A)):
        #performing pivoting
        Partial_pivot.solve(A, A)
        pivot = A[r1][r1]
        #column loop
        for c1 in range(len(A[r1])):
            A[r1][c1] = A[r1][c1]/pivot
        for r2 in range(len(A)):
            if r2 == r1 or A[r2][r1] == 0:
                pass
            else:
                factor = A[r2][r1]
                for c1 in range(len(A[r2])):
                    A[r2][c1] = A[r2][c1] - factor * A[r1][c1]
    # solutions printing
    print("The solutions are: ")
    for r1 in range(len(A)):
        print("X", r1+1, "=", round(A[r1][3]))