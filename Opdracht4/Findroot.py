import bisection
import math


f1 = lambda x: x*x -2
bisection.findAllroots(f1,-2,2,0.01)
print('-----------------------------------------------------------------------')
f2 = lambda x:math.sin(math.pi*x)
bisection.findAllroots(f2,1,9.5,0.01)