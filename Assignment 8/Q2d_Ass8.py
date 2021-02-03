import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import my_library as ml


def fun(x,y,z):
    return ((x**2)/(1**2))+((y**2)/(1.5**2))+((z**2)/(2**2))


N = 10000
Fn, X1, X2, Y1, Y2, Z1, Z2, frac_err = ml.monte_carlo_volume(-1,1,-1.5,1.5,-2,2,fun,N)

print("\nVolume = ", Fn)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X1, Y1, Z1)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()



'''


Volume =  12.5856


'''