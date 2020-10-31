import my_library

#Creat data file for plotting pi vs N graph
file = open("datas_Q4_montecarlo.txt", "w+")

#define function
def fun(x):
    return (4/(1 + (x**2)))

#limits
a = 0
b = 1
#no. of random values
N = 100000

#calling function
intg = my_library.monte_carlo(a, b, fun, N, file)
print("Integration of the function = ", intg)

## -:The Exact Output appended below:-##
'''
Integration of the function =  3.1416513746167505
'''