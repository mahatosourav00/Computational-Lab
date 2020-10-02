# import libraries

import my_library
import math

# open required text files for saving datas for plotting

#for Q1a
f0 = open("datas_Q1a_Bisection.txt","w+")
f1 = open("datas_Q1a_Regula_falsi.txt","w+")
f2 = open("datas_Q1a_Newton-Raphson.txt","w+")


#for Q1b
g0 = open("datas_Q1b_Bisection.txt","w+")
g1 = open("datas_Q1b_Regula_falsi.txt","w+")
g2 = open("datas_Q1b_Newton-Raphson.txt","w+")



#initial guesses
a = 1.5
b = 2.5


print("\n-----!!!! QUESTION 1a !!!!-----")

#Question 1(i)
#define function for (logx-sinx) given on Q1(i)
def fun_q1a(x):
    return (math.log(x) - math.sin(x))


#root using bisection method
print("\nThe value of root is (BY BISECTION) :", my_library.bisection(a, b, fun_q1a, f0))

#root using regula falsi metod
print("\nThe value of root is (BY REGULA FALSI :", my_library.regula_falsi(a, b, fun_q1a, f1))

#root using newton raphson method
print("\nThe value of root is (BY NEWTON RAPHSON) :", my_library.newton_raphson(b, fun_q1a, f2))


print("\n\n-----!!!! QUESTION 1b !!!!-----")

#Question 1(i)

#define function for (-x-cosx) given on Q1(ii)
def fun_q1b(x):
    return (- x - math.cos(x))


#initial guesses

a = -1
b = 1


#root using bisection method
print("\nThe value of root is (BY BISECTION) :", my_library.bisection(a, b, fun_q1b, g0))

#root using regula falsi metod
print("\nThe value of root is (BY REGULA FALSI) :", my_library.regula_falsi(a, b, fun_q1b, g1))

#root using newton raphson method
print("\nThe value of root is (BY NEWTON RAPHSON) :", my_library.newton_raphson(a, fun_q1b, g2))



#### ---- THE EXACT OUTPUT IS ----- ####

"""

-----!!!! QUESTION 1a !!!!-----

-----BISECTION METHOD-----
Iterations   Absolute error
     1       5.000e-01   
     2       2.500e-01   
     3       1.250e-01   
     4       6.250e-02   
     5       3.125e-02   
     6       1.562e-02   
     7       7.812e-03   
     8       3.906e-03   
     9       1.953e-03   
     10      9.766e-04   
     11      4.883e-04   
     12      2.441e-04   
     13      1.221e-04   
     14      6.104e-05   
     15      3.052e-05   
     16      1.526e-05   
     17      7.629e-06   
     18      3.815e-06   
     19      1.907e-06   
     20      9.537e-07   

The value of root is (BY BISECTION) : 2.2191076278686523

-----REGULA FALSI------
Iterations   Absolute error
     1       6.507e-01   
     2       6.359e-02   
     3       4.499e-03   
     4       3.070e-04   
     5       2.089e-05   
     6       1.421e-06   
     7       9.672e-08   

The value of root is (BY REGULA FALSI : 2.2191071418525734

-----NEWTON-RAPHSON------
Iterations   Absolute error
     1       2.686e-01   
     2       1.242e-02   
     3       9.132e-05   
     4       9.645e-07   

The value of root is (BY NEWTON RAPHSON) : 2.2191071388563035


-----!!!! QUESTION 1b !!!!-----

-----BISECTION METHOD-----
Iterations   Absolute error
     1       1.000e+00   
     2       5.000e-01   
     3       2.500e-01   
     4       1.250e-01   
     5       6.250e-02   
     6       3.125e-02   
     7       1.562e-02   
     8       7.812e-03   
     9       3.906e-03   
     10      1.953e-03   
     11      9.766e-04   
     12      4.883e-04   
     13      2.441e-04   
     14      1.221e-04   
     15      6.104e-05   
     16      3.052e-05   
     17      1.526e-05   
     18      7.629e-06   
     19      3.815e-06   
     20      1.907e-06   
     21      9.537e-07   

The value of root is (BY BISECTION) : -0.7390851974487305

-----REGULA FALSI------
Iterations   Absolute error
     1       4.597e-01   
     2       1.877e-01   
     3       1.052e-02   
     4       5.302e-04   
     5       2.657e-05   
     6       1.331e-06   
     7       6.666e-08   

The value of root is (BY REGULA FALSI) : -0.7390851296998365

-----NEWTON-RAPHSON------
Iterations   Absolute error
     1       2.527e-01   
     2       8.298e-03   
     3       7.482e-05   
     4       8.064e-07   

The value of root is (BY NEWTON RAPHSON) : -0.7390851246291479


"""