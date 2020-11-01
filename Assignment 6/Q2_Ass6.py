import my_library

#define function
def fun(x):
    return (x/(1 + x))

#limits
a = 1
b = 3

#For N = 5
N = 5
print("For N = 5:")
ans51 = my_library.midpoint(a, b, fun, N)
print("Itegral(Midpoint) = ", ans51)
ans52= my_library.traphezoidal(a, b, fun, N)
print("Itegral(Trapezoidal) = ", ans52)
#due to odd no. issue with simpson method we take N=(Even no.)
if (N % 2) != 0:
    N = N+1
    print("Due to odd no. issue with simpson method, we take N=(N+1) i.e N =", N)
ans63 = my_library.simpson(a, b, fun, N)
print("Itegral(Simpson) = ", ans63)

#For N = 10
N = 10
print("\nFor N = 10:")
ans101 = my_library.midpoint(a, b, fun, N)
print("Itegral(Midpoint) = ", ans101)
ans102 = my_library.traphezoidal(a, b, fun, N)
print("Itegral(Trapezoidal) = ", ans102)
if (N % 2) != 0:
    N = N+1
    print("Due to odd no. issue with simpson method, we take N=(N+1) i.e N =", N)
ans103 = my_library.simpson(a, b, fun, N)
print("Itegral(Simpson) = ", ans103)


#For N = 25
N = 25
print("\nFor N = 25:")
ans251 = my_library.midpoint(a, b, fun, N)
print("Itegral(Midpoint) = ", ans251)
ans252 = my_library.traphezoidal(a, b, fun, N)
print("Itegral(Trapezoidal) = ", ans252)
#due to odd no. issue with simpson method we take N=(Even no.)
if (N % 2) != 0:
    N = N+1
    print("Due to odd no. issue with simpson method, we take N=(N+1) i.e N =", N)
ans263 = my_library.simpson(a, b, fun, N)
print("Itegral(Simpson) = ", ans263)

#print the comparison on tabulated form
print("\n\n-:Comparison of the results of the integral methods with actual analytical result:-")

print("\n--------------------------------------------------------------------------")
print(" {:<5}| {:<15} {:<25}| {:<12}".format("N", "Method", "Result (Integral)", "Actual Analytical value"))
print("--------------------------------------------------------------------------")
print(" {:<5}| {:<15} {:<25}| {:<12}".format(" ", "Midpoint",ans51 , " "))
print(" {:<5}| {:<15} {:<25}| {:<12}".format("5", "Traphezoidal",ans52 , " "))
print(" {:<5}| {:<15} {:<25}| {:<12}".format(" ", "Simpson(N=6)",ans63 , " "))
print("------------------------------------------------")
print(" {:<5}| {:<15} {:<25}| {:<12}".format(" ", "Midpoint",ans101 , " "))
print(" {:<5}| {:<15} {:<25}| {:^20}".format("10", "Traphezoidal",ans102 , "1.306852819440055"))
print(" {:<5}| {:<15} {:<25}| {:<12}".format(" ", "Simpson",ans103 , " "))
print("------------------------------------------------")
print(" {:<5}| {:<15} {:<25}| {:<12}".format(" ", "Midpoint",ans251 , " "))
print(" {:<5}| {:<15} {:<25}| {:<12}".format("25", "Traphezoidal",ans252 , " "))
print(" {:<5}| {:<15} {:<25}| {:<12}".format(" ", "Simpson(N=26)",ans263 , " "))

print("--------------------------------------------------------------------------")



## -:The Exact Output appended below:-##
'''
For N = 5:
Itegral(Midpoint) =  1.308092114284065
Itegral(Trapezoidal) =  1.3043650793650796
Due to odd no. issue with simpson method, we take N=(N+1) i.e N = 6
Itegral(Simpson) =  1.306830206830207

For N = 10:
Itegral(Midpoint) =  1.3071646395900398
Itegral(Trapezoidal) =  1.3062285968245722
Itegral(Simpson) =  1.3068497693110697

For N = 25:
Itegral(Midpoint) =  1.3069028019555275
Itegral(Trapezoidal) =  1.3067528394240817
Due to odd no. issue with simpson method, we take N=(N+1) i.e N = 26
Itegral(Simpson) =  1.3068527513069683


-:Comparison of the results of the integral methods with actual analytical result:-

--------------------------------------------------------------------------
 N    | Method          Result (Integral)        | Actual Analytical value
--------------------------------------------------------------------------
      | Midpoint        1.308092114284065        |             
 5    | Traphezoidal    1.3043650793650796       |             
      | Simpson(N=6)    1.306830206830207        |             
------------------------------------------------
      | Midpoint        1.3071646395900398       |             
 10   | Traphezoidal    1.3062285968245722       |  1.306852819440055  
      | Simpson         1.3068497693110697       |             
------------------------------------------------
      | Midpoint        1.3069028019555275       |             
 25   | Traphezoidal    1.3067528394240817       |             
      | Simpson(N=26)   1.3068527513069683       |             
--------------------------------------------------------------------------

'''