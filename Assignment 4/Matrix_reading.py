def read(B):
    #read the matrix text files
    a = open(B)
    A = []
    #A matrix
    for i in a:
        A.append([int(j) for j in i.split()])
    return (A)
