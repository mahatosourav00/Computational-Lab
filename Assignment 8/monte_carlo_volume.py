import  random


X1 = []
X2 = []
Y1 = []
Y2 = []
Z1 = []
Z2 = []
analyt_val = 12.57

def monte_carlo_volume(a1, a2, b1, b2, c1, c2, fun, N):
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
    return Fn, X1, X2, Y1, Y2, Z1, Z2, frac_err