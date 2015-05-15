import bisection
import math

def f1(x):
    return float(x*(x-1)-1)
root = bisection.findroot(f1,-10,10,0.01)
print('---------------------------------------------')
def f2(x):
    return float(x*x)
    
root = bisection.findroot(f2,-8,10,0.01)
print('---------------------------------------------')
root = bisection.findroot(math.cos,-10,10,0.01)