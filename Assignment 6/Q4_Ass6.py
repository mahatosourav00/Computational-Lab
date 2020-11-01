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

#set the time for how long the monte carlo fuction will run(more time means more no. of N)
duration = 4        #The funtion will run for 4 seconds

#calling function
intg = my_library.monte_carlo(a, b, fun, duration, file)
print("Integration of the function = ", intg)

## -:The Exact Output appended below:-##
'''
Integration of the function =  3.1415730638082224
'''