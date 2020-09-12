#read the libraries
import Partial_pivot
import LU_decomposition
import Forward_substitution
import Backward_substitution
import Matrix_reading
import Matrix_printing

A = Matrix_reading.read("Q1_MatrixA.txt")
#print A matrix
print("\nA matrix is = ")
Matrix_printing.printit(A)

B = Matrix_reading.read("Q1_MatrixB.txt")
#print B matrix
print("\nB matrix is = ")
Matrix_printing.printit(B)

#partial pivot of MAtrix A
A = Partial_pivot.solve(A, B)


#Call LU decomposition library and perform it
A = LU_decomposition.solve(A)


#Call Forward substition library and solve Y matrix(LY = B)
B = Forward_substitution.solve(A, B)


#Call Backward substition library and solve X matrix(UX = Y)
B = Backward_substitution.solve(A, B)

#print the solutions
print("\nThe calculated solutions are: ")
for i in range(len(B)):
    print("X", i+1 ,"=", B[i][0])


#### ---- THE EXACT OUTPUT IS ----- ####

"""
A matrix is = 
1  0  1  2  
0  1  -2  0  
1  2  -1  0  
2  1  3  -2  

B matrix is = 
6  
-3  
-2  
0  

Lower Triangular Matrix is = 
1.0  0.0  0.0  0.0  
0.0  1.0  0.0  0.0  
1.0  2.0  1.0  0.0  
2.0  1.0  1.5  1.0  

Upper Triangular Matrix is = 
1  0  1  2  
0.0  1.0  -2.0  0.0  
0.0  0.0  2.0  -2.0  
0.0  0.0  0.0  -3.0  

The calculated solutions are: 
X 1 = 1.0
X 2 = -1.0
X 3 = 1.0
X 4 = 2.0

"""