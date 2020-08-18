A = [2, 3, 4]
B = [5, 6, 7]
add = []
product = 0
print("Two vectors are A = ", A, "and B = ", B)
for i in range(len(A)):
    add.append(A[i] + B[i])
print("Vector sum = ", add)

for i in range(len(A)):
    product = product + (A[i]*B[i])

print("Dot product = ", product)