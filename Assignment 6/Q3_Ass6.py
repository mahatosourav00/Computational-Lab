import my_library
import math

#define function
def fun(x):
    return math.exp(-(x**2))

#limits
a = 0
b = 1

#Max error given in question
max_error = 0.001

#Peak point for different order of derivarion of the function on the limit 0,1
sec_der_f_max = -2
four_der_f_max = 12

#midpoint
print("----------------------------------------------")
print("--:Midpoint Method:--")
print("----------------------------------------------")
N = (my_library.max_error_midpoint(a, b, sec_der_f_max, max_error))
print("Calculated 'N' (Max. Error = 0.001) =", N)
ans = my_library.midpoint(a, b, fun, N)
print("Integral =", ans)
print("----------------------------------------------")

#trapezoidal
print("\n----------------------------------------------")
print("--:Trapezoidal Method:--")
print("----------------------------------------------")
N = (my_library.max_error_trapezoidal(a, b, sec_der_f_max, max_error))
print("Calculated 'N' (Max. Error = 0.001) =", N)
ans = my_library.traphezoidal(a, b, fun, N)
print("Integral =", ans)
print("----------------------------------------------")

#Simpson Method
print("\n----------------------------------------------")
print("--:Simpson Method:--")
print("----------------------------------------------")
N = (my_library.max_error_simpson(a, b, four_der_f_max, max_error))
print("Calculated 'N' (Max. Error = 0.001) =", N)
if (N % 2) != 0:
    N = N+1
    print("Due to odd no. issue with simpson method, we take N=(N+1) i.e N =", N)
ans = my_library.simpson(a, b, fun, N)
print("Integral =", ans)
print("----------------------------------------------")

## -:The Exact Output appended below:-##
'''
----------------------------------------------
--:Midpoint Method:--
----------------------------------------------
Calculated 'N' (Max. Error = 0.001) = 10
Integral = 0.7471308777479975
----------------------------------------------

----------------------------------------------
--:Trapezoidal Method:--
----------------------------------------------
Calculated 'N' (Max. Error = 0.001) = 13
Integral = 0.7464612610366896
----------------------------------------------

----------------------------------------------
--:Simpson Method:--
----------------------------------------------
Calculated 'N' (Max. Error = 0.001) = 3
Due to odd no. issue with simpson method, we take N=(N+1) i.e N = 4
Integral = 0.7468553797909873
----------------------------------------------

'''
