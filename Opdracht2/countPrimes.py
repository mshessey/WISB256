import sys
import math
if len(sys.argv) is not 2:
    print('Bad input. Wrong number of arguments. Format should be: $ python3 countPrimes.py <input filename>')
    print('Aborting...')
    sys.exit()
#readfile = open(str(sys.argv[1]), 'r')
C  = 0.6601618
number = int(0)
lastnumber = int(100)
pi = int(0)
pi2 = int(0)
with open(sys.argv[1]) as readfile:
    for line in readfile:
        pi += 1
        number = int(line.rstrip())
        #print(number)
        if number - lastnumber == 2:
            pi2 += 1
        lastnumber = number
        
NlogN = number / math.log(number)
LittleHardy = 2*C*number /(math.log(number)**2)
ratio1 = pi/NlogN
ratio2 = pi2/LittleHardy
print('Number {} || pi(N) {} || N/log(N) {} || ratio {} || pi2(N) {} || 2CN/log(N)^2 {} || ratio {} '.format(number,pi,NlogN,ratio1,pi2,LittleHardy,ratio2))

