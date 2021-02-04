import math
import random
import time
import matplotlib.pyplot as plt



def least_square_fit_linear(X, Y):
    sum_x = 0
    sum_y = 0
    sum_x2 = 0
    sum_y2 = 0
    sum_xy = 0
    n = len(X)
    for i in range(len(X)):
        sum_x = sum_x + X[i]
        sum_y = sum_y + Y[i]
        sum_x2 = sum_x2 + (X[i]**2)
        sum_y2 = sum_y2 + (Y[i]**2)
        sum_xy = sum_xy + (X[i]*Y[i])

    avg_x = sum_x/n
    avg_y = sum_y/n

    c = ((avg_y*sum_x2)-(avg_x * sum_xy))/(sum_x2-(n*(avg_x**2))) #a
    m = (sum_xy - (n*avg_x*avg_y))/(sum_x2-(n*(avg_x**2)))        #b

    Sxx = sum_x2 - n*(avg_x**2)
    Syy = sum_y2 - n*(avg_y**2)
    Sxy = sum_xy - n*avg_x*avg_y

    sigx2 = Sxx/n   #variance
    sigy2 = Syy/n
    covari = Sxy/n   #covariance

    r = math.sqrt(Sxy**2/(Sxx*Syy))

    s = math.sqrt((Syy - (Sxy**2/Sxx))/(n-2))
    sd_c = s * math.sqrt((1/n)+((avg_x**2)/Sxx))
    sd_m = s/(math.sqrt(Sxx))


    return m, c, Sxx, Syy, Sxy, r, sd_c, sd_m


def least_square_fit_polynomial(A):
    gauss_jordan(A)
    for i in range(len(A)):
        print("a", i,"=", A[i][len(A[i])-1])



#########################################################
def random_walk(M, N):

    random.seed(None)
    r2 = 0
    R2 = []
    X = []
    Y = []
    sum_r2 = 0
    for j in range(0, M):

        X1 = []
        Y1 = []
        x = 0.0
        y = 0.0
        r2 = 0.0
        X1.append(x)
        Y1.append(y)

        for i in range(0, N):
            theta = 2 * math.pi * random.random()
            x1 = math.cos(theta)
            y1 = math.sin(theta)
            x = x + x1
            y = y + y1
            X1.append(x)
            Y1.append(y)
        X.append(X1)
        Y.append(Y1)
        r2 = x ** 2 + y ** 2
        R2.append(r2)
    sum_r2 = 0
    for i in range(len(R2)):
        sum_r2 = sum_r2 + R2[i]

    avg_r2 = sum_r2 / len(R2)
    r_rms = math.sqrt(avg_r2)

    sum_x = 0
    sum_y = 0
    for i in range(len(X)):
        sum_x = sum_x + X[i][len(X[i]) - 1]
        sum_y = sum_y + Y[i][len(Y[i]) - 1]

    avg_x = sum_x / len(X)
    avg_y = sum_y / len(Y)
    rad_dis = math.sqrt(avg_x ** 2 + avg_y ** 2)

    return X, Y, r_rms, avg_x, avg_y, rad_dis




def monte_carlo_volume(a1, a2, b1, b2, c1, c2, fun, N, analyt_val):
    X1 = []
    Y1 = []
    Z1 = []
    vol_box = (a2 - a1) * (b2 - b1) * (c2 - c1)
    Fn = 0
    inte = 0

    for i in range(N):
        x = random.uniform(a1, a2)
        y = random.uniform(b1, b2)
        z = random.uniform(c1, c2)

        if (fun(x, y, z) <= 1):
            X1.append(x)
            Y1.append(y)
            Z1.append(z)
            inte = inte + 1
    Fn = (vol_box/float(N)) * inte
    frac_err = abs(Fn - analyt_val)/analyt_val
    return Fn, X1, Y1, Z1, frac_err








#####################################################################


def eular_forward(x0, y0, h, fun, n, file):
    file.write("{:<15}{:<15}\n".format(x0, y0))
    copyx = x0
    copyy = y0
    while round(x0,6) > 0:
        y = y0 - h * fun(x0, y0)
        x0 = x0 - h
        y0 = y
        file.write("{:<15.6}{:<15.10}\n".format(x0, y0))
    x0 = copyx
    y0 = copyy
    while round(x0,6) < n:
        y = y0 + h * fun(x0, y0)
        x0 = x0 + h
        y0 = y
        file.write("{:<15.6}{:<15.10}\n".format(x0, y0))
    file.close()

def runge_kutta_4(x0, y0, z0, h, fun1, fun2, n, file):
    file.write("{:<15}{:<15}\n".format(x0, y0))
    while round(x0,6) < n:
        k1y = h * fun1(x0, y0, z0)
        k1z = h * fun2(x0, y0, z0)
        k2y = h * fun1((x0 + h/2), (y0 + k1y/2), (z0 + k1z/2))
        k2z = h * fun2((x0 + h/2), (y0 + k1y/2), (z0 + k1z/2))
        k3y = h * fun1((x0 + h/2), (y0 + k2y/2), (z0 + k2z/2))
        k3z = h * fun2((x0 + h/2), (y0 + k2y/2), (z0 + k2z/2))
        k4y = h * fun1((x0 + h), (y0 + k3y), (z0 + k3z))
        k4z = h * fun2((x0 + h), (y0 + k3y), (z0 + k3z))
        y = y0 + (1/6 * (k1y + (2 * k2y) + (2 * k3y) + k4y))
        z0 = z0 + (1/6 * (k1z + (2 * k2z) + (2 * k3z) + k4z))
        x0 = x0 + h
        y0 = y
        file.write("{:<15.6}{:<15.10}\n".format(x0, y0))
    return y0

def shoting_method(x0, y0, zh0, zl0, xn, yn, h, fun1, fun2, file1, file2):
    yh = runge_kutta_4(x0, y0, zh0, h, fun1, fun2, xn, file1)
    yl = runge_kutta_4(x0, y0, zl0, h, fun1, fun2, xn, file2)
    if yh > yn and yl < yn:
        while abs(yh - yn) > 0.001 or abs(yl - yn) > 0.001:
            if abs(yh - yn) > abs(yn - yl):
                zh0 = zl0 + (((zh0 - zl0)/(yh - yl)) * (yn - yl))

            elif abs(yh - yn) < abs(yn - yl):
                zl0 = zl0 + (((zh0 - zl0) / (yh - yl)) * (yn - yl))
            yh = runge_kutta_4(x0, y0, zh0, h, fun1, fun2, xn, file1)
            yl = runge_kutta_4(x0, y0, zl0, h, fun1, fun2, xn, file2)
    elif yh < yn and yl < yn:
        print("Yh for current zh =", yh)
        return print("please change your 'zh' ")

    elif yh > yn and yl > yn:
        print("Yl for current zl =", yl)
        return print("please change your 'zl' ")

    elif yh < yn and yl > yn:
        print("Yh for current zh =", yh)
        print("Yl for current zl =", yl)
        return print("please change your 'zl' and 'zh'")
    return zh0, yh



#########################################################################

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
    # due to odd no. issue with simpson method we take N=(Even no.)
    if (N % 2) != 0:
        N = N + 1
        print("Due to odd no. issue with simpson method, we take N=(N+1) i.e N =", N)
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

def monte_carlo(a, b, fun, duration, file):
    Fn = 0
    sum_fx = 0
    #print("\nN = ", N)
    i = 1
    #store the time before running the loop
    start_time = time.time()
    #difference between current time and start time
    runtime = time.time()-start_time
    #run the loop for given duration of time
    while (runtime <= duration):
        #generate random no,
        x = random.random()
        x = a + ((b - a)*x)
        fx = fun(x)
        sum_fx = sum_fx + fx
        Fn = ((b - a)/(i+1)) * sum_fx
        i = i+1
        runtime = time.time() - start_time
        #print("runtime = ", (time.time()-start_time))
        #when i is multiple of 10, store value of i and value of pi for that i on text file for plotting
        if (i % 10) == 0:
            file.write("{:<15}{:<20}\n".format((i), Fn))
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


    #do bracketing
    a, b = bracketing(a, b, func)
    # define minimum difference b/w a and b
    eps = 0.000001
    i = 0
    c = 0
    #printing on tabulated form


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
       # print("{:^12} {:<12.3e}".format(i, error))
    file.close()
    # if 200 iteration completed
    if i >= 200:
        print("!!!Maximum no. of iterations done on bisection!!\n", "Please change your a and b")
    #if not
    else:
        return c



#define regula falsi function
def regula_falsi(a, b, func, file):

    #do bracketing
    bracketing(a, b, func)
    eps = 0.000001
    i = 0
    c = a
    copy = c + 1
    #printing on tabulated form

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
        #print("{:^12} {:<12.3e}".format(i, error))
    file.close()
    # restrict to 200 iteration
    if i >= 200:
        print("!!!Maximum no. of iterations done on regula falsi!!!\n", "Please change your a and b")
    else:
        return c



#define Newton-Raphson function
def newton_raphson(x0, func, file, eps):
    x1 = x0 + 1
    i = 0

    error = abs (x1 - x0)
    # do newton raphson and limit iteration to 200
    while error >= eps and i < 200:
        i = i+1
        x1 = x0 - (func(x0) / first_deri(x0, func))
        error = abs(x1-x0)
        file.write("{:^12} {:<12.3e}\n".format(i, error))
        #print("{:^12} {:<12.3e}".format(i, error))
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
    return coeffs



#function for determining roots of polynomial function
def polynomial_root(coefficients, alpha):
    global coeffs, n
    ans = []
    coeffs = coefficients
    n = len(coeffs)
    while n > 1:
        alpha = laguerre(alpha, n)
        ans.append(alpha)
        print("\nX", 6 - n, " = ", alpha)
        synthetic_division(coeffs, alpha)
        n = n-1
    return ans


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
    return A




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

def make_matrix(N, M):
    I = [[0 for x in range(M)] for y in range(N)]
    return I