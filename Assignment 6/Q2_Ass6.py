import my_library

#define function
def fun(x):
    return (x/(1 + x))

#limits
a = 1
b = 3

#For N = 5
print("For N = 5:")
ans51 = my_library.midpoint(a, b, fun, 5)
print("Itegral(Midpoint) = ", ans51)
ans52= my_library.traphezoidal(a, b, fun, 5)
print("Itegral(Trapezoidal) = ", ans52)
ans53 = my_library.simpson(a, b, fun, 5)
print("Itegral(Simpson) = ", ans53)

#For N = 10
print("\nFor N = 10:")
ans101 = my_library.midpoint(a, b, fun, 10)
print("Itegral(Midpoint) = ", ans101)
ans102 = my_library.traphezoidal(a, b, fun, 10)
print("Itegral(Trapezoidal) = ", ans102)
ans103 = my_library.simpson(a, b, fun, 10)
print("Itegral(Simpson) = ", ans103)


#For N = 25
print("\nFor N = 25:")
ans251 = my_library.midpoint(a, b, fun, 25)
print("Itegral(Midpoint) = ", ans251)
ans252 = my_library.traphezoidal(a, b, fun, 25)
print("Itegral(Trapezoidal) = ", ans252)
ans253 = my_library.simpson(a, b, fun, 25)
print("Itegral(Simpson) = ", ans253)

#print the comparison on tabulated form
print("\n\n-:Comparison of the results of the integral methods with actual analytical result:-")

print("\n--------------------------------------------------------------------------")
print(" {:<5}| {:<15} {:<25}| {:<12}".format("N", "Method", "Result (Integral)", "Actual Analytical value"))
print("--------------------------------------------------------------------------")
print(" {:<5}| {:<15} {:<25}| {:<12}".format(" ", "Midpoint",ans51 , " "))
print(" {:<5}| {:<15} {:<25}| {:<12}".format("5", "Traphezoidal",ans52 , " "))
print(" {:<5}| {:<15} {:<25}| {:<12}".format(" ", "Simpson",ans53 , " "))
print("------------------------------------------------")
print(" {:<5}| {:<15} {:<25}| {:<12}".format(" ", "Midpoint",ans101 , " "))
print(" {:<5}| {:<15} {:<25}| {:^20}".format("10", "Traphezoidal",ans102 , "1.306852819440055"))
print(" {:<5}| {:<15} {:<25}| {:<12}".format(" ", "Simpson",ans103 , " "))
print("------------------------------------------------")
print(" {:<5}| {:<15} {:<25}| {:<12}".format(" ", "Midpoint",ans251 , " "))
print(" {:<5}| {:<15} {:<25}| {:<12}".format("25", "Traphezoidal",ans252 , " "))
print(" {:<5}| {:<15} {:<25}| {:<12}".format(" ", "Simpson",ans253 , " "))

print("--------------------------------------------------------------------------")



## -:The Exact Output appended below:-##
'''
For N = 5:
Itegral(Midpoint) =  1.308092114284065
Itegral(Trapezoidal) =  1.3043650793650796
Itegral(Simpson) =  1.3068497693110697

For N = 10:
Itegral(Midpoint) =  1.3071646395900398
Itegral(Trapezoidal) =  1.3062285968245722
Itegral(Simpson) =  1.3068526253348838

For N = 25:
Itegral(Midpoint) =  1.3069028019555275
Itegral(Trapezoidal) =  1.3067528394240817
Itegral(Simpson) =  1.3068528144450458


-:Comparison of the results of the integral methods with actual analytical result:-

--------------------------------------------------------------------------
 N    | Method          Result (Integral)        | Actual Analytical value
--------------------------------------------------------------------------
      | Midpoint        1.308092114284065        |             
 5    | Traphezoidal    1.3043650793650796       |             
      | Simpson         1.3068497693110697       |             
------------------------------------------------
      | Midpoint        1.3071646395900398       |             
 10   | Traphezoidal    1.3062285968245722       |  1.306852819440055  
      | Simpson         1.3068526253348838       |             
------------------------------------------------
      | Midpoint        1.3069028019555275       |             
 25   | Traphezoidal    1.3067528394240817       |             
      | Simpson         1.3068528144450458       |             
--------------------------------------------------------------------------

'''