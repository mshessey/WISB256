import operator

opdracht = input()
words = opdracht.split()
ops = {'+' : operator.add, '-' : operator.sub, '*' : operator.mul, '/': operator.truediv}
#answer = ops[words[2]](int(words[0]),int(words[1]))

while True:
    #print('Looking for words')
    #print(words)
    alreadyfound = False
    if len(words) > 1:
       # print('There are still words')
        for i in range(0,len(words)):
            if alreadyfound:
                break
          #  print('Trying word--: '+str(words[i]))
            for sign in ops:
            #    print('Trying sign: '+str(sign))
                if words[i] == sign:
               #     print('Word matched sign')
                    words[i] = ops[words[i]](int(words[i-2]),int(words[i-1]))
                 #   print(words)
                    words.pop(i-2)
                   # print(words)
                    words.pop(i-2)
                   # print(words)
                    alreadyfound = True
                    break
                else:
                    continue
    else:
        break

answer = words[0] 
answer = "{0:.3f}".format(answer)
print(answer)