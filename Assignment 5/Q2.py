#import library

import my_library

# make list of coefficients of given polynomial equation on decreasing order of power
coeff_poly_q2 = [1, -3, -7, 27, -18]

# initial guess
alpha = 1.5

#get roots using lagurre method and synthetic division
print("\n----The Roots are:----")
my_library.polynomial_root(coeff_poly_q2, alpha)



#### ---- THE EXACT OUTPUT IS ----- ####

"""

----The Roots are:----

X 1  =  2.0000000770712423
Coefficients:  [1, -0.9999999229287577, -8.999999922928751, 8.999999460501325, -3.8535621271762466e-07]

X 2  =  0.9999999447575642
Coefficients:  [1, 2.1828806429091685e-08, -8.999999901099946, 5.65832962706736e-08, -3.287729195727502e-07]

X 3  =  2.9999999726022546
Coefficients:  [1, 2.999999994431061, 1.7763568394002505e-15, 5.658330159974407e-08, -1.5902301632377285e-07]

X 4  =  -2.999999994431061
Coefficients:  [1, 0.0, 1.7763568394002505e-15, 5.658329627067356e-08, -3.287729048206846e-07]

"""