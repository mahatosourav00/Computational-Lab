import math
import random

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
