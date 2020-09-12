#read the libraries
import Partial_pivot
import LU_decomposition
import Forward_substitution
import Backward_substitution


#read the matrix text files
a = open("Q1_MatrixA.txt")
b = open("Q1_MatrixB.txt")
A = []
B = []
#A matrix
for i in a:
    A.append([int(j) for j in i.split()])

#print A matrix
print("\nA matrix is = ")
for i in A:
    for j in i:
        print(j, end='  ')
    print()

#B matrix
for i in b:
    B.append([int(j) for j in i.split()])

#print B matrix
print("\nB matrix is = ")
for i in B:
    for j in i:
        print(j, end='  ')
    print()

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