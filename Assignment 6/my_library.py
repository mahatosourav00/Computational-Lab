import math
import random

def max_error_midpoint(a, b, sec_der_f_max, max_error):
    err = (math.sqrt((((b-a)**3)*abs(sec_der_f_max))/(24*max_error)))
    return math.ceil(err)

def max_error_trapezoidal(a, b, sec_der_f_max, max_error):
    err = (math.sqrt((((b-a)**3)*abs(sec_der_f_max))/(12*max_error)))
    return math.ceil(err)

def max_error_simpson(a, b, four_der_f_max, max_error):
    err = (((((b-a)**5)*abs(four_der_f_max))/(180*max_error))**(1/4))
    return math.ceil(err)

def midpoint(a, b, fun, N):
    h = (b - a)/N
    #print("h = ", h)
    sum = 0
    for i in range(1, N+1):
        xi = ((a + (i-1)*h) + (a + i*h))/2
        area = h * fun(xi)
        sum = sum + area
        #print("sum = ", sum)
    return sum


def traphezoidal(a, b, fun, N):
    h = (b - a)/N
    sum = 0
    for i in range(N):
        x0 = a + i*h
        x1 = a + (i + 1)*h
        area = h/2*(fun(x0) + fun(x1))
        sum = sum + area
        #print("sum = ", sum)
    return sum

def simpson(a, b, fun, N):
    h = (b - a)/N
    sum = 0
    for i in range(0, N, 2):
        x0 = a + i*h
        x2 = a + (i+2)*h
        h1 = (x2 - x0)/2
        x1 = (x2 + x0)/2
        intg = (h1/3)*(fun(x0) + 4*fun(x1) + fun(x2))
        sum = sum + intg
    return sum

def monte_carlo(a, b, fun, N, file):
    #print(" {:<12}| {:<20}".format("N", "Integral (Value of pi)"))
    Fn = 0
    sum_fx = 0
     #print("\nN = ", N)
    for i in range(N):
        x = random.random()
        x = a + ((b - a)*x)
        fx = fun(x)
        sum_fx = sum_fx + fx
        Fn = ((b - a)/(i+1)) * sum_fx
        #print("Integration of the function = ", Fn)
        #print(" {:<12}| {:<20}".format((i+1), Fn))
        file.write("{:<15}{:<20}\n".format((i+1), Fn))
    #print("Integration of the function = ", Fn)
    file.close()
    return Fn





#########################################################################

def first_deri(x, func):
    h = 0.4
    return (func(x+h) - func(x-h))/(2*h)


def sec_deri(x, func):
    h = 0.4
    return (func(x+h) + func(x-h) - 2 * func(x))/(2*h*h)

# Define bracketing function
def bracketing(a, b, func):
    #factor assumption
    beta = 1.5

    i = 0
    #checking a and b is already bracketed or not
    #if yes
    if func(a) * func(b) < 0:
        pass
    #if not, bracket it and limit the iteration to 13
    elif func(a) * func(b) > 0:
        while func(a) * func(b) > 0 and i < 13:
            i = i + 1
            if abs(func(a)) < abs(func(b)):
                a = a - beta * (b - a)
            elif abs(func(a)) > abs(func(b)):
                b = b + beta * (b - a)
    # if 13 iteration completed
    if i >= 13:
        print("!!!Maximum no. of iterations done on bracketing!!!\n", "Please change your a and b")
    #if not
    else:
        return(a, b)



# Define Bisection function
def bisection(a, b, func, file):
    print("\n-----BISECTION METHOD-----")

    #do bracketing
    a, b = bracketing(a, b, func)
    # define minimum difference b/w a and b
    eps = 0.000001
    i = 0
    c = 0
    #printing on tabulated form
    print("{:<12} {:<12}".format("Iterations", "Absolute error"))

    #do bisection while |b-a| >= eps and limit the iteratio to 200
    while abs(b - a) >= eps and i < 200:
        i = i+1
        copy = c
        c = (a + b) / 2
        if func(a) * func(c) < 0:
            copy = b
            b = c
        elif func(a) * func(c) > 0:
            copy = a
            a = c
        error = abs(c - copy)
        file.write("{:^12} {:<12.3e}\n".format(i, error))
        print("{:^12} {:<12.3e}".format(i, error))
    file.close()
    # if 200 iteration completed
    if i >= 200:
        print("!!!Maximum no. of iterations done on bisection!!\n", "Please change your a and b")
    #if not
    else:
        return c



#define regula falsi function
def regula_falsi(a, b, func, file):
    print("\n-----REGULA FALSI------")
    #do bracketing
    bracketing(a, b, func)
    eps = 0.000001
    i = 0
    c = a
    copy = c + 1
    #printing on tabulated form
    print("{:<12} {:<12}".format("Iterations", "Absolute error"))
    # do regula falsi while |previous c - current c| >= eps and limit the iteratio to 200
    while abs(c - copy) >= eps and i < 200:
        i = i + 1
        copy = c
        c = b - (((b - a) * func(b)) / (func(b) - func(a)))
        if (func(a) * func(c)) < 0:
            b = c
        else:
            a = c
        error = abs(c - copy)
        file.write("{:^12} {:<12.3e}\n".format(i, error))
        print("{:^12} {:<12.3e}".format(i, error))
    file.close()
    # restrict to 200 iteration
    if i >= 200:
        print("!!!Maximum no. of iterations done on regula falsi!!!\n", "Please change your a and b")
    else:
        return c



#define Newton-Raphson function
def newton_raphson(x0, func, file):
    print("\n-----NEWTON-RAPHSON------")
    eps = 0.000001
    x1 = x0 + 1
    i = 0
    print("{:<12} {:<12}".format("Iterations", "Absolute error"))
    error = abs (x1 - x0)
    # do newton raphson and limit iteration to 200
    while error >= eps and i < 200:
        i = i+1
        x1 = x0 - (func(x0) / first_deri(x0, func))
        error = abs(x1-x0)
        file.write("{:^12} {:<12.3e}\n".format(i, error))
        print("{:^12} {:<12.3e}".format(i, error))
        x0 = x1
    file.close()
    # if 200 iteration completed
    if i >= 200:
        print("!!!Maximum no. of iterations done on Newton-Raphson!!!\n", "Please change your a and b")
    #if not
    else:
        return x1



#polynomial function
def polynomial_func(x, n, coeffs):
    sum = 0
    for i in range(1, n+1):
        if i == n:
            sum = sum + coeffs[i-1]
        else:
            sum  = sum + coeffs[i-1] * x**(n-i)
    return sum



#function for calling polynomial function with global variables
def poly_func(x):
    return polynomial_func(x, n, coeffs)



#laguerre method
def laguerre(a0, n):
    #check whether initial guess is itself a function or not
    #if not
    if poly_func(a0) != 0:
        eps = 0.000001
        i = 0
        a1 = a0 + 1
        #perform lagurre and limit the iteration to 200
        while abs(a1 - a0) >= eps and i < 200:
            i = i+1
            a1 = a0
            G = first_deri(a0, poly_func) / poly_func(a0)
            H = (G * G) - (sec_deri(a0, poly_func) / poly_func(a0))
            denom1 = (G + math.sqrt((n - 1)*(n * H - (G**2))))
            denom2 = (G - math.sqrt((n - 1)*(n * H - (G**2))))
            if abs(denom1) > abs(denom2):
                a = n / denom1
            else:
                a = n / denom2
            a0 = a0 - a
    return a0



#function for synthetic division
def synthetic_division(coeffs, a):
    #make coeff of highest power |1|
    if abs(coeffs[0] != 1):
        for i in range(len(coeffs)):
            coeffs[i] = coeffs[i]/ coeffs[0]

    #perfom symthetic division
    for i in range(1, len(coeffs)):
        coeffs[i] = coeffs[i] + a * coeffs[i-1]
    print("Coefficients: ", coeffs)
    return coeffs



#function for determining roots of polynomial function
def polynomial_root(coefficients, alpha):
    global coeffs, n
    coeffs = coefficients
    n = len(coeffs)
    while n > 1:
        alpha = laguerre(alpha, n)
        print("\nX", 6 - n, " = ", alpha)
        synthetic_division(coeffs, alpha)
        n = n-1



def partial_pivot(A, B):

    # row loop for checking 0 on diagonal positions
    for r1 in range(len(A)-1):
        if abs(A[r1][r1]) == 0:
            # row loop for finding suitable row for interchanging
            for r2 in range(r1 + 1, len(A)):
                # row interchange
                if A[r2][r1] > A[r1][r1]:
                    a1 = A[r1]
                    A[r1] = A[r2]
                    A[r2] = a1
                    b1 = B[r1]
                    B[r1] = B[r2]
                    B[r2] = b1
    #return the A matrix
    return (A)



def gauss_jordan(A):
    #row loop
    for r1 in range(len(A)):
        #performing pivoting
        partial_pivot(A, A)
        pivot = A[r1][r1]
        #column loop
        for c1 in range(len(A[r1])):
            A[r1][c1] = A[r1][c1]/pivot
        for r2 in range(len(A)):
            if r2 == r1 or A[r2][r1] == 0:
                pass
            else:
                factor = A[r2][r1]
                for c1 in range(len(A[r2])):
                    A[r2][c1] = A[r2][c1] - factor * A[r1][c1]
    # solutions printing
    print("The solutions are: ")
    for r1 in range(len(A)):
        print("X", r1+1, "=", round(A[r1][3]))



def lu_decomposition(A):
    n = len(A)

    #perform LU Decomposition
    #Both Upper and Lower triangular matrix will be stored on A matrix together
    for j in range(n):

        # upper trianguar matrix
        for i in range(j+1):
            sum = 0
            for k in range(i):
                sum = sum + A[i][k] * A[k][j]
            #store to A matrix
            A[i][j] = A[i][j] - sum

        #lower triangular matrix
        for i in range(j+1, n):
            sum = 0
            for k in range(j):
                sum = sum + A[i][k] * A[k][j]
            # store to M matrix
            A[i][j] = (A[i][j] - sum)/A[j][j]


    #print Lower triangual matrix from A matrix
    print("\nLower Triangular Matrix is = ")
    for i in range(n):
        for j in range(len(A[i])):
            if j > i:
                print("0.0", end='  ')
            elif j == i:
                print("1.0", end='  ')
            else:
                print(A[i][j], end='  ')
        print()

    #print Upper triangular matrix from A matrix
    print("\nUpper Triangular Matrix is = ")
    for i in range(n):
        for j in range(len(A[i])):
            if j < i:
                print("0.0", end='  ')
            else:
                print(A[i][j], end='  ')
        print()

    return (A)



def forward_substitution(L, B):

    #creat Y matrix
    Y = [[0] for i in range(len(L))]

    # calculate Y matrix
    for i in range(len(L)):
        sum = 0
        for j in range (i+1):
            if i == j:
                pass
            else:
                sum = sum + L[i][j] * Y[j][0]
        Y[i][0] = (B[i][0] - sum)

    #return the calculated Y matrix
    return (Y)



def backward_substituition(U, Y):
    # creat x matrix
    X = [[0] for i in range(len(U))]

    # calculate x matrix
    for i in range(len(U) - 1, -1, -1):
        sum = 0
        for j in range(len(U) - 1, i - 1, -1):
            sum = sum + U[i][j] * X[j][0]
        X[i][0] = (Y[i][0] - sum) / U[i][i]

    # return the calculated x matrix
    return (X)



def matrix_multiplication(A, B):
    n= len(A)
    AB =  [[0.0 for j in range(n)] for i in range(n)]
    for i in range(len(A)):
        for j in range(len(B[i])):
            add = 0
            for k in range(len(A[i])):
                multiply = (A[i][k] * B[k][j])
                add = add + multiply
            AB[i][j] = add
    return (AB)




def matrix_read(B):
    #read the matrix text files
    a = open(B)
    A = []
    #A matrix
    for i in a:
        A.append([int(j) for j in i.split()])
    return (A)



def matrix_print(A):
    for i in A:
        for j in i:
            print(j, end='  ')
        print()