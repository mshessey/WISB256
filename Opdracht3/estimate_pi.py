import random
import math
import sys

############################## Check User Input
if len(sys.argv) is 4:
    try: 
        myseed = int(sys.argv[3])
    except:
        print('Seed must be of type int')
        sys.exit()
    else:
        random.seed(myseed)
elif len(sys.argv) is not 3:
    print('Use:  estimate_pi.py N L (optional: Seed)')
    sys.exit()
try:
    N = int(sys.argv[1])
except ValueError:
    print('First argument must be of type int')
    sys.exit()
except:
    print('Unknown error with first argument')
    sys.exit()
try:
    L = float(sys.argv[2])
except ValueError:
    print('Second argument must be of type float')
    sys.exit()
except:
    print('Unknown error with second argument')
    sys.exit()

#if L > 1.:
   # print('AssertionError: L should be less than or equal to 1')
   # sys.exit()
if L <= 0.:
    print('AssertionError: L should be greater than 0')
    sys.exit()

######################################### function declaration
def drop_needle(L):
    x0 = random.random()
    theta = random.uniform(0,2*math.pi)
    x1 = x0 + math.cos(theta) * L
    #print(str(type(x1)))
    #print(str(type(y1)))
    if x1 < 0. or x1 > 1.:
        #print('x1: '+str(x1)+' y1: '+str(y1))
        return True

    else:
        return False
        
def drop_needle_better(L):
    y = random.uniform(0,1)
    theta = random.uniform(0,math.pi/2)
    if L *math.cos(theta)>y:
        return True
    return False
########################################### initialise non user input:
hits = 0
pi = float(0)
#Pinv = float(0)
########################################### Actual program
for i in range(0,int(N)):
    if drop_needle(L):
        hits += 1

if L < 1:
    P = float(hits) / float(N)
    pi = 2*L / P
elif L >= 1:
    P = float(hits) / float(N)
    upper = 2*L - 2*(math.sqrt(L**2-1)+math.asin(1/L))
    lower = P-1
    pi = upper /lower
print(str(int(hits)) + ' hits in ' +str(N)+' tries')
print('Pi = '+str(pi))