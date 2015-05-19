import operator

opdracht = input()
words = opdracht.split()
ops = {'+' : operator.add, '-' : operator.sub, '*' : operator.mul, '/': operator.truediv}
#answer = ops[words[2]](int(words[0]),int(words[1]))

while True:
    alreadyfound = False
    if len(words) > 1:
        for i in range(0,len(words)):
            if alreadyfound:
                break
            for sign in ops:
                if words[i] == sign:
                    words[i] = ops[words[i]](float(words[i-2]),float(words[i-1]))
                    words.pop(i-2)
                    words.pop(i-2)
                    alreadyfound = True
                    break
                else:
                    continue
    else:
        break

answer = words[0] 
answer = "{0:.3f}".format(answer)
print(answer)