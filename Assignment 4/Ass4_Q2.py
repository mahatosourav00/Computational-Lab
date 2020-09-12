#import required libraries
import Partial_pivot
import LU_decomposition
import Forward_substitution
import Backward_substitution
import Matrix_reading
import Matrix_printing

#read matrix from file
A = Matrix_reading.read("Q2_MatrixA.txt")

#print A matrix
print("\nA matrix is = ")
Matrix_printing.printit(A)

n = len(A)
#Creat identity matrix
I = [[0 for x in range(n)] for y in range(n)]
for i in range(n):
    I[i][i] = 1


#partial pivot to remove zeros from the diagonal entries
Partial_pivot.solve(A, I)
for i in A:
    for j in i:
        print(j, end=' ')
    print()


#check inverse of the matrix is possible or not by calculating determinant of matrix
#A)after calculating Lower and upper triangular matrix of A, store it on A matrix
#B) Determinant = Multiplication of diagonal entries of new A matrix

# A) part
A = LU_decomposition.solve(A)

# B) part
multiply = 1
for i in range(n):
    multiply = multiply * A[i][i]

#print determinant
print("\nDeterminant of the matrix =", multiply)

#check the determinat is non zero or not, therefore inverse of the matrix exist or not.
if multiply == 0:
    print("\nThe determinant of matrix is zero.\n\n'THE INVERSE OF THE MATRIX DOES NOT EXISTS'")
else:
    print("The matrix has non zero determinant.\n\n'THE INVERSE OF THE MATRIX EXISTS'")


    #calculate inverse
    #solve Ly = b for each column of unit matrix followed by solving Ux = y.

    for j in range(n):
        B = [[I[i][j]] for i in range(n)]
        B = Forward_substitution.solve(A, B)
        B = Backward_substitution.solve(A, B)

        #storing each column of calculated inverse on the I matrix
        for i in range(n):
            I[i][j] = B[i][0]

    #print the I matrix for displaying inverse matrix
    print("\nThe inverse of the matrix is = ")
    for i in I:
        for j in i:
            print(round(j, 4), end=' ')
        print()

#### ---- THE EXACT OUTPUT IS ----- ####

"""
The matrix is = 
3 7 1 0 
0 2 8 6 
0 0 1 2 
0 1 0 1 

Lower Triangular Matrix is = 
1.0  0.0  0.0  0.0  
0.0  1.0  0.0  0.0  
0.0  0.0  1.0  0.0  
0.0  0.5  -4.0  1.0  

Upper Triangular Matrix is = 
3  7  1  0  
0.0  2.0  8.0  6.0  
0.0  0.0  1.0  2.0  
0.0  0.0  0.0  6.0  

Determinant of the matrix = 36.0
The matrix has non zero determinant.

'THE INVERSE OF THE MATRIX EXISTS'

The inverse of the matrix is = 
-0.25 1.6667 -1.8333 0.3333 
0.0833 -0.6667 0.8333 0.0 
0.1667 -0.3333 -0.3333 0.0 
-0.0833 0.6667 0.1667 0.0 

"""