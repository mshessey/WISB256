smax = int(input())
toeschouwers = input()
staand = 0
vrienden = 0

for s in range (0,smax+1):
   # print('Checking s: '+str(s))
    while True:
        comp = staand+vrienden
  #      print('Comparing s = '+str(s)+' with staand+vrienden = '+str(comp))
        if s <= comp:
 #           print('s <= comp')
            staand = staand + int(toeschouwers[s])
            break
        else:
#            print('s > comp')
            vrienden += 1


#print('Final output: ')
print(str(vrienden))