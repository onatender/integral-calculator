def fonksiyon(x):
    return x**2 + 2*x + 1


def turev(x,depth):
    return (fonksiyon(x+(10**(-1*depth))) - fonksiyon(x))/((x+(10**(-1*depth)))-x)

#print(abs(turev(25,8)))

def integral(x0,x1,fx,depth):
    diff = 10**(-1*depth)
    sum = 0
    while x0 < x1:
        sum += abs(fx(x0)*(diff))
        x0 += diff
    return sum

def f(x):
    return x**2 + 2*x + 1

# x^3 / 3 + x^2 +x +c
# (125 / 3 + 25 + 5 + c) - (0 + 0 + 0 + c)
# 125/3 + 30
# 71.6666666

for i in range(1,8):
    print(f"depth:{i}, result:",integral(x0=0,x1=5,fx=f,depth=i))
    
