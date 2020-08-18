#read matrix files
m = open("MatrixM.txt")
n = open("MatrixN.txt")
M = []
N = []
for i in m:
    M.append([int(j) for j in i.split()])
for i in n:
    N.append([int(j) for j in i.split()])
print("M = ")
for i in M:
    for j in i:
        print(j, end=' ')
    print()
print("\nN = ")
for i in N:
    for j in i:
        print(j, end=' ')
    print()
#define matrix A
A = [[14, 18], [12, 26], [21, 32]]
print("\nA = ")
for i in A:
    for j in i:
        print(j, end=' ')
    print()

#M*A
MA = [0] * 3
for i in range(3):
    MA[i] = [0] * 2
for i in range(len(M)):
    for j in range(len(A[i])):
        add = 0
        for k in range(len(M[i])):
            multiply = (M[i][k]*A[k][j])
            add = add + multiply
        MA[i][j] = add
print("\nM*A = ")

for i in MA:
    for j in i:
        print(j, end=' ')
    print()

#M*N
MN = [0] * 3
for i in range(3):
    MN[i] = [0] * 3
for i in range(len(M)):
    for j in range(len(N[i])):
        add = 0
        for k in range(len(M[i])):
            multiply = (M[i][k]*N[k][j])
            add = add + multiply
        MN[i][j] = add

print("\nM*N = ")
for i in MN:
    for j in i:
        print(j, end=' ')
    print()