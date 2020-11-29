import my_library

file1 = open("Datas_Q3h_p01.txt", "w+")
file2 = open("Datas_Q3l_p01.txt", "w+")

def deff_fun2(x, y, z):
    return (z+1)

def deff_fun1(x, y, z):
    return (z)

x0 = 0
y0 = 1
zh0 = 2
zl0 = 0

xn = 1
yn = 2 * (2.71828 - 1)


h = 0.01

my_library.shoting_method(x0, y0, zh0, zl0, xn, yn, h, deff_fun1, deff_fun2, file1, file2)


'''
---:Output:---

-: For boundary condition (Given on problem), Yn =  3.43656 :-
After Langarangian interpolation we got, The value of Z = 0.9999978720203274
And for Z = 0.9999978720203274 , The calculated value of Yn = 3.4365600000000023

'''