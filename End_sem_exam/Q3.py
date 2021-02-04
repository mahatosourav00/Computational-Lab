import sourav_mahato_my_library as ml
import matplotlib.pyplot as plt
import math
#open file containing datas
f = open("esem_table.dat")

A = []
#taking datas to a list
for i in f:
    A.append([j for j in i.split()])

#extracting x and y datas from A list
X = []
Y = []
for i in range(2, len(A)-1):
    X.append(float(A[i][0]))
    Y.append(float(A[i][1]))

#i) fit using w(t) = w0 + wc*t
m, c, Sxx, Syy, Sxy, r, sd_c, sd_m = ml.least_square_fit_linear(X,Y)

print("\ni)Fitting of data using w(t) = w0 + wc*t")
print("Wc =", m)
print("W0 =",c)

#print("Sx = ", Sxx)
#print("Sy = ", Syy)
#print("Sxy = ", Sxy)
print("Standard deviation on W0 = ", sd_c)
print("Standard deviation on Wc = ", sd_m)


print("Pearson r i.e. Quality of fit = ", r)

#creat fitted Y datas
y_fit_a = []
for i in range(len(X)):
    y_fit_a.append(c + float(m)*(X[i]))

#plotting
plt.figure()
plt.title("Fitting using w(t) = w0 + wc*t")
plt.xlabel("time")
plt.ylabel("angular velocity")
plt.plot(X, y_fit_a, "--r")
plt.scatter(X,Y)
plt.grid()
plt.show()


#i) fit using w(t) = w0*exp(-wc*t)

#w(t) = w0*exp(-wc*t)
# Therefore, -> log(w(t)) = log(w0) - wc*t

Xb = []
Yb = []

for i in range(len(Y)):
    Yb.append(math.log(Y[i]))

mb, cb, Sxxb, Syyb, Sxyb, rb, sd_cb, sd_mb = ml.least_square_fit_linear(X,Yb)

#as, cb = log(w0)
w0 = math.exp(cb)

#creat fitted Y datas
y_fit_b = []
for i in range(len(X)):
    y_fit_b.append(w0*math.exp(mb*X[i]))   #-ve sign on exponantial part is already embebbed on the calculated constant by fitting

print("\nii)Fitting of data using w(t) = w0*exp(-wc*t)")
print("Wc =", mb)
print("W0 =",cb)

#print("Sx = ", Sxx)
#print("Sy = ", Syy)
#print("Sxy = ", Sxy)
print("Standard deviation on W0 = ", sd_cb)
print("Standard deviation on Wc = ", sd_mb)

print("Pearson r i.e. Quality of fit = ", rb)

#plotting
plt.figure()
plt.title("Fitting using w(t) = w0*exp(-wc*t)")
plt.xlabel("time")
plt.ylabel("angular velocity")
plt.plot(X, y_fit_b, "--r")
plt.scatter(X,Y)
plt.grid()
plt.show()



'''

i)Fitting of data using w(t) = w0 + wc*t
Wc = -0.4747086247086251
W0 = 2.0291025641025655
Standard deviation on W0 =  0.05095705145102608
Standard deviation on Wc =  0.026157630469407007
Pearson r i.e. Quality of fit =  0.9851557666128388

ii)Fitting of data using w(t) = w0*exp(-wc*t)
Wc = -0.3955961745485569
W0 = 0.7902775293458726
Standard deviation on W0 =  0.01024259029790577
Standard deviation on Wc =  0.005257798173814032
Pearson r i.e. Quality of fit =  0.9991179387307727



'''