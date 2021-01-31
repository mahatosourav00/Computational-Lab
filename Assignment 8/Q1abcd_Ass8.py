import random_walk as rw
import matplotlib.pyplot as plt
import math

figure, axes = plt.subplots(nrows=2, ncols=3)


RMS = []
steps = []

M = 100
N = 250
add = 200
print("\n\nFor Steps = 250; No. of walks = 100 : ")

X1, Y1, r_rms1, avg_x1, avg_y1, rad_dis1 = rw.random_walk(M, N)

print("Rrms = ", r_rms1)
print("rootN = ",math.sqrt(N))
print("Average X = ", avg_x1)
print("Average Y = ", avg_y1)
print("Radial distance R = ", rad_dis1)

RMS.append(r_rms1)
steps.append(math.sqrt(N))
for i in range(5):
    axes[0, 0].set_xlabel('X')
    axes[0, 0].set_ylabel('Y')
    axes[0, 0].grid(True)
    axes[0, 0].set_title("For steps = 250; walks = 100")
    axes[0,0].plot(X1[i],Y1[i])



N = N + add
print("\n\nFor Steps =", N,"; No. of walks =",M, ": ")
X2, Y2, r_rms2, avg_x2, avg_y2, rad_dis2 = rw.random_walk(M, N)

print("Rrms = ", r_rms2)
print("rootN = ",math.sqrt(N))
print("Average X = ", avg_x2)
print("Average Y = ", avg_y2)
print("Radial distance R = ", rad_dis2)
RMS.append(r_rms2)
steps.append(math.sqrt(N))

for i in range(5):
    axes[0, 1].set_xlabel('X')
    axes[0, 1].set_ylabel('Y')
    axes[0,1].grid(True)
    axes[0,1].set_title("For steps = 450; walks = 100")
    axes[0,1].plot(X2[i],Y2[i])


N = N + add
print("\n\nFor Steps =", N,"; No. of walks =",M, ": ")
X3, Y3, r_rms3, avg_x3, avg_y3, rad_dis3 = rw.random_walk(M, N)

print("Rrms = ", r_rms3)
print("rootN = ",math.sqrt(N))
print("Average X = ", avg_x3)
print("Average Y = ", avg_y3)
print("Radial distance R = ", rad_dis3)

RMS.append(r_rms3)
steps.append(math.sqrt(N))

for i in range(5):
    axes[0, 2].set_xlabel('X')
    axes[0, 2].set_ylabel('Y')
    axes[0, 2].grid(True)
    axes[0, 2].set_title("For steps = 650; walks = 100")
    axes[0,2].plot(X3[i],Y3[i])


N = N + add
print("\n\nFor Steps =", N,"; No. of walks =",M, ": ")
X4, Y4, r_rms4, avg_x4, avg_y4, rad_dis4 = rw.random_walk(M, N)

print("Rrms = ", r_rms4)
print("rootN = ",math.sqrt(N))
print("Average X = ", avg_x4)
print("Average Y = ", avg_y4)
print("Radial distance R = ", rad_dis4)

RMS.append(r_rms4)
steps.append(math.sqrt(N))

for i in range(5):
    axes[1, 0].set_xlabel('X')
    axes[1, 0].set_ylabel('Y')
    axes[1, 0].grid(True)
    axes[1, 0].set_title("For steps = 850; walks = 100")
    axes[1, 0].plot(X4[i],Y4[i])

N = N + add
print("\n\nFor Steps =", N,"; No. of walks =",M, ": ")

X5, Y5, r_rms5, avg_x5, avg_y5, rad_dis5 = rw.random_walk(M, N)

print("Rrms = ", r_rms5)
print("rootN = ",math.sqrt(N))
print("Average X = ", avg_x5)
print("Average Y = ", avg_y5)
print("Radial distance R = ", rad_dis5)
RMS.append(r_rms5)
steps.append(math.sqrt(N))


for i in range(5):
    axes[1, 1].set_xlabel('X')
    axes[1, 1].set_ylabel('Y')
    axes[1, 1].grid(True)
    axes[1, 1].set_title("For steps = 1050; walks = 100")
    axes[1,1].plot(X5[i],Y5[i])
#figure.tight_layout()
plt.figure()
plt.title("Rrms vs root of N plot for Steps(N) = 250, 450, 650, 850, 1050.")
plt.ylabel('Rrms')
plt.xlabel('Root of N')
plt.plot(steps, RMS)

plt.grid(True)
plt.show()


'''

For Steps = 250; No. of walks = 100 : 
Rrms =  15.811388300841896
rootN =  15.811388300841896
Average X =  -0.6642855229541521
Average Y =  -1.8163263829958007
Radial distance R =  1.9339898618072122


For Steps = 450 ; No. of walks = 100 : 
Rrms =  21.213203435596427
rootN =  21.213203435596427
Average X =  -0.6690185189290166
Average Y =  1.9612009334904328
Radial distance R =  2.0721715373476495


For Steps = 650 ; No. of walks = 100 : 
Rrms =  25.495097567963924
rootN =  25.495097567963924
Average X =  -3.9589058216858115
Average Y =  -0.01568804701423124
Radial distance R =  3.9589369052558707


For Steps = 850 ; No. of walks = 100 : 
Rrms =  29.154759474226502
rootN =  29.154759474226502
Average X =  0.7830463010112522
Average Y =  -1.2441552410116083
Radial distance R =  1.4700625065840085


For Steps = 1050 ; No. of walks = 100 : 
Rrms =  32.4037034920393
rootN =  32.4037034920393
Average X =  -1.6909341611311712
Average Y =  -3.858484911314333
Radial distance R =  4.212738319445056



'''