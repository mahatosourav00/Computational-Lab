#define function for partial pivot
def partial_pivot(A):
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

#define function  for gauss jordan method
def gauss_jordon(A):
    #row loop
    for r1 in range(len(A)):
        #performing pivoting
        partial_pivot(A)
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
    c = 119
    for r1 in range(len(A)):
        c = c + 1
        print(chr(c),"=", round(A[r1][3]))

print("Please enter the Question no. (allowed values = 1-2), you want to get the solution: ")
inp = int(input())
# Question no. 1
if  inp == 1:
    # reading the text files
    a = open("MatrixQ1.txt")
    A = []
    for i in a:
        A.append([int(j) for j in i.split()])
    # performing gauss jordan
    print("The equations to be solved are:\nx + 3y + 2z = 2 \n2x + 7y + 7z = -1 \n2x + 5y + 2z = 7\n")
    gauss_jordon(A)
    '''
    The solutions are :
        x = 3.0
        y = 1.0
        z = -2.0
    '''
# Question no. 2
elif inp == 2:
    # reading the text files
    a = open("MatrixQ2.txt")
    A = []
    for i in a:
        A.append([int(j) for j in i.split()])
    # performing gauss jordan
    print("The equations to be solved are:\n2y + 5z = 1 \n3x - y + 2z = -2 \nx - y + 3z = 3\n")
    gauss_jordon(A)
    '''
     The solutions are :
        x = -2.0
        y = -2.0
        z = 1.0
    '''