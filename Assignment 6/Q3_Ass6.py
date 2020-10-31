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
ans = my_library.simpson(a, b, fun, N)
print("Integral =", ans)
print("----------------------------------------------")

## -:The Exact Output appended below:-##
'''
----------------------------------------------
--:Midpoint Method:--
----------------------------------------------
Calculated 'N' (Max. Error = 0.001) = 13
Integral = 0.747005595525096
----------------------------------------------

----------------------------------------------
--:Trapezoidal Method:--
----------------------------------------------
Calculated 'N' (Max. Error = 0.001) = 19
Integral = 0.7466542743612604
----------------------------------------------

----------------------------------------------
--:Simpson Method:--
----------------------------------------------
Calculated 'N' (Max. Error = 0.001) = 5
Integral = 0.7468249482544437
----------------------------------------------


'''
