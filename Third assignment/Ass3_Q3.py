#define function for partial pivot
def partial_pivot(A, B):
    # row loop for checking 0 on diagonal positions
    for r1 in range(len(A)-1):
        if abs(A[r1][r1]) == 0:
            # row loop for finding suitable row for interchanging
            for r2 in range(r1 + 1, len(A)):
                # row interchange
                if A[r2][r1] > A[r1][r1]:
                    a1 = A[r1]
                    A[r1] = A[r2]
                    A[r2] = a1
                    b1 = B[r1]
                    B[r1] = B[r2]
                    B[r2] = b1

#define function  for gauss jordan method
def gauss_jordon(A, B):
    #row loop
    for r1 in range(len(A)):
        # performing pivoting
        partial_pivot(A, B)
        pivot = A[r1][r1]
        #column loop
        for c1 in range(len(A[r1])):
            A[r1][c1] = A[r1][c1]/pivot
        for c2 in range(len(B[r1])):
            B[r1][c2] = B[r1][c2] / pivot
        for r2 in range(len(A)):
            if r2 == r1 or A[r2][r1] == 0:
                pass
            else:
                factor = A[r2][r1]
                for c1 in range(len(A[r2])):
                    A[r2][c1] = A[r2][c1] - factor * A[r1][c1]
                for c2 in range(len(B[r1])):
                    B[r2][c2] = B[r2][c2] - factor * B[r1][c2]

def matrix_multiplication(A, B):
    AB = [0] * 3
    for i in range(3):
        AB[i] = [0] * 3
    for i in range(len(A)):
        for j in range(len(B[i])):
            add = 0
            for k in range(len(A[i])):
                multiply = (A[i][k] * B[k][j])
                add = add + multiply
            AB[i][j] = add
    print("\nThe multiplication of The Matrix and its Inverse is = ")

    for i in AB:
        for j in i:
            print(round(j), end='  ')
        print()
# reading the text file
a = open("MatrixQ3.txt")
ac = open("MatrixQ3.txt")
A = []
AC = []
uM = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
for i in a:
    A.append([int(j) for j in i.split()])
for i in ac:
    AC.append([int(j) for j in i.split()])
#printing the matrix given in the question
print("The Matrix is = ")
for i in AC:
    for j in i:
        print(j, end='  ')
    print()
#printing the calculated inverse of the given matrix
gauss_jordon(A, uM)
print("\nThe Inverse of the Matrix is")
for i in uM:
    for j in i:
        print(round(j, 4), end='  ')
    print()
    '''
    The output for inverse matrix is :
        -3.0  3.0  -7.0
        1.0  1.0  0.0
        1.0  0.0  1.0
    '''


#multiplication of the matrix and its inverse
matrix_multiplication(AC, uM)
'''
The output for the multiplication of given matrix and its inverse is
    1  0  0
    0  1  0
    0  0  1
'''