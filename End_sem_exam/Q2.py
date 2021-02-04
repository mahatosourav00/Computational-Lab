import math
import sourav_mahato_my_library as ml

a = math.sin(math.pi/8)

L = 1
g = 9.8

def fun(x):
    return 1/math.sqrt(1 - (a**2)*(math.sin(x))**2)

ub = math.pi/2
lb = 0

N = 10

inte = ml.simpson(lb,ub,fun,N)


ans = inte * (4*math.sqrt(L/g))
print("The time period, T = ", ans,"sec")


'''

The time period, T =  2.0873200174795916 sec

'''