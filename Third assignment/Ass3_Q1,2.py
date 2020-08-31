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
        #performing pivoting
        partial_pivot(A, B)
        pivot = A[r1][r1]
        #column loop
        for c1 in range(len(A[r1])):
            A[r1][c1] = A[r1][c1]/pivot
        for c2 in range(len(B[r1])):
            B[r1][c2] = B[r1][c2]/pivot
        for r2 in range(len(A)):
            if r2 == r1 or A[r2][r1] == 0:
                pass
            else:
                factor = A[r2][r1]
                for c1 in range(len(A[r2])):
                    A[r2][c1] = A[r2][c1] - factor * A[r1][c1]
                for c2 in range(len(B[r1])):
                    B[r2][c2] = B[r2][c2] - factor * B[r1][c2]
    # solutions printing
    print("The solutions are: ")
    c = 119
    for r1 in B:
        c = c + 1
        for r2 in r1:
            print(chr(c),"=",round(r2, 4), end=' ')
        print()

print("Please enter the Question no. (allowed values = 1-2), you want to get the solution: ")
inp = int(input())
# Question no. 1
if  inp == 1:
    # reading the text files
    a = open("MatrixQ1A.txt")
    b = open("MatrixQ1B.txt")
    A = []
    B = []
    for i in a:
        A.append([int(j) for j in i.split()])
    for i in b:
        B.append([int(j) for j in i.split()])
    # performing gauss jordan
    print("The equations to be solved are:\nx + 3y + 2z = 2 \n2x + 7y + 7z = -1 \n2x + 5y + 2z = 7\n")
    gauss_jordon(A, B)
    '''
    The solutions are :
        x = 3.0
        y = 1.0
        z = -2.0
    '''
# Question no. 2
elif inp == 2:
    # reading the text files
    a = open("MatrixQ2A.txt")
    b = open("MatrixQ2B.txt")
    A = []
    B = []
    for i in a:
        A.append([int(j) for j in i.split()])
    for i in b:
        B.append([int(j) for j in i.split()])
    # performing gauss jordan
    print("The equations to be solved are:\n2y + 5z = 1 \n3x - y + 2z = -2 \nx - y + 3z = 3\n")
    gauss_jordon(A, B)
    '''
     The solutions are :
        x = -2.0
        y = -2.0
        z = 1.0
    '''