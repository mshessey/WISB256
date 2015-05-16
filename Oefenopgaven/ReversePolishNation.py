import operator

opdracht = input()
words = opdracht.split()
ops = {'+' : operator.add, '-' : operator.sub, '*' : operator.mul, '/': operator.truediv}
answer = ops[words[2]](int(words[0]),int(words[1]))
answer = "{0:.3f}".format(answer)
print(answer)