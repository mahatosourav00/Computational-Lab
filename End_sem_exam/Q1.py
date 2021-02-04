import sourav_mahato_my_library as ml
import math
#creat file for save iteration datas
f = open("Q1_datas.txt", "w+")

h = 6.626*(10**(-34))
k = 1.381*(10**(-23))
c = 3*(10**8)

eps = 0.0001

x0 = 10

def func(x):
    return ((x - 5)*(math.exp(x)) + 5)


#x = h*c/lambda*K*T
#lambda*K = b
#b = h*c/k*x
def func_x(x):
    return (h*c)/(k*x)

#calculate the root of the equation
x_root = ml.newton_raphson(x0,func,f,eps)
print("x =", x_root)

#calculate b
b = func_x(x_root)

print("b =", b)

print("The value of weins constant b is = ", b,"K-m")



'''

x = 4.965115312644961
b = 0.002899009699626615
The value of weins constant b is =  0.002899009699626615 K-m


'''