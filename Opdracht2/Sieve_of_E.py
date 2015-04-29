import sys
import time
########################################### check user input
#print('Just checking: you input', len(sys.argv), 'arguments.')
#print('Argument List:', str(sys.argv))
if len(sys.argv) is not 3:
    print('Bad input. Wrong number of arguments. Format should be: $ python3 Sieve_of_E.py <number> <output filename>')
    print('Aborting...')
    sys.exit()
try:
    number = int(sys.argv[1])
except ValueError:
    print('Bad input. 1st variable should be of type int')
    print('Aborting...')
    sys.exit()
except:
    print('Bad input / unexpected error. Check arguments')
    print('Aborting...')
    sys.exit()
if not '.dat' in str(sys.argv[2]):
    print('Bad file specifier as 2nd argument')
    print('Aborting...')
    sys.exit()
T1 = time.perf_counter()
file = open(str(sys.argv[2]),'w')
######################################## Actual sieve part:
primes = [2]
if number%2 == 0:
    odds = (number-2) /2
else:
    odds = (number-3)/2

odds = int(odds)
#print(odds)
ismarked = [False] * odds
for oddcounter in range (0,odds):
    ##debug
   # value = oddcounter*2 +3
    #print('Considering the odd number with index: '+str(oddcounter) +' and value:'+ str(value))
    ##end debug
    if ismarked[oddcounter]:
        # not a prime, already marked
        continue
    else:
        # prime found, add to list, start sieving
        value = oddcounter*2 +3
        #print('Found prime: '+str(value))
        primes.append(value)
        sieve = 2*oddcounter**2+6*oddcounter+3 #find the counter which goes with the square of the prime
        while(sieve < odds):
           # checkvalue = sieve*2 + 3
           # print('For prime: '+str(value)+' sieving oddnumber '+str(sieve)+' with value: '+str(checkvalue)) 
            ismarked[sieve] = True
            sieve = sieve + value
############################################## end of sieve
T2 = time.perf_counter()
timetaken = T2-T1
primesfound = len(primes)
print('Found ' + str(primesfound) + ' Prime numbers smaller than ' + str(number) + ' in ' + str(timetaken) +' sec.') 
for x in range(0,len(primes)):
    file.write(str(primes[x])+ "\n")
file.close()