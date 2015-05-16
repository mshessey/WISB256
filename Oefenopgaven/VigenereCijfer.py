alphabet = 'abcdefghijklmnopqrstuvwxyz'
def tonumber(a):
    value = 0
    for i in alphabet:
        if i == a:
            return value
        else:
            value += 1
            
def tochar(num):
    value = 0
    for i in alphabet:
        if value == num:
            return i
        else:
            value += 1

def getoutchar(letter,codeletter):
    letnum = tonumber(letter)
    codenum = tonumber(codeletter)
    outnum = (letnum - codenum) % 26
    outchar = str(tochar(outnum))
    return outchar
    
jumbled = input()
code = input()
size = len(code)
output = []
pos = 0
for letter in jumbled:
    codeletter = code[pos]
    outchar = getoutchar(letter,codeletter)
    output.append(outchar)
    pos +=1
    if pos == size:
        pos = 0
output = ''.join(output)
print(output)