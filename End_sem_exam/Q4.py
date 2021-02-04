import sourav_mahato_my_library as ml

#creat file for save iteration datas
f1 = open("Q4_datas_zh0.txt", "w+")
f2 = open("Q4_datas_zl0.txt", "w+")

#at time t=0
t0 = 0
y0 = 2
#at time t = n
tn = 5
yn = 45
g = 9.8


#dy/dx = z and dz/dx = -g

def func1(x, y, z):
    return z

def func2(x, y, z):
    return (-g)

h = 0.002

zl0 = 30
zh0 =35

zh1, yh = ml.shoting_method(t0,y0,zh0,zl0,tn,yn,h,func1,func2,f1,f2)
f1.close()
f2.close()
print("zh0= ", zh1)
print("Therefore, The launch velocity =", zh1, "m/s")


'''

zh0=  33.10000000000026
Therefore, The launch velocity = 33.10000000000026 m/s

'''