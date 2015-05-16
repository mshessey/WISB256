line1 = input()
line2 = input()
line3 = input()

game = [line1,line2,line3]

def horwin(line):
    original = line[0]
    if original == '0':
        return 'NO'
    for i in line:
        if i != original:
            return 'NO' #no one
    return original


def vertwin(col):
    original=line1[col]
    if original == '0':
        return 'NO'
    for line in game:
        if line[col] != original:
            return 'NO'
    return original
    
def downdiagwin():
    original = game[0][0]
    if original == '0':
        return 'NO'
    for i in range(1,3):
        if game[i][i] != original:
           # print('Tested: '+str(game[i][i])+' Against: '+str(original))
            return 'NO'
    return original
    
def updiagwin():
    original = game[2][0]
    if original == '0':
        return 'NO'
    for i in range(1,3):
        if game[2-i][i] != original:
            return 'NO'
    return original



def findwinner():
    ret = downdiagwin()
    if ret != 'NO':
            #print('downdiagwin')
            return ret
    ret = updiagwin()
    if ret != 'NO':
            #print('updiagwin')
            return ret
    for i in range (0,3):
        ret = horwin(game[i])
        if ret != 'NO':
           # print('horwin in line: '+str(i))
            return ret
        ret = vertwin(i)
        if ret != 'NO':
            #print('verwin in col: '+str(i))
            return ret
    return 'NO'   

output = 'No winner'

if findwinner()=='1':
    output = 'Player 1 wins'
    
if findwinner()=='2':
    output = 'Player 2 wins'
    
print(output)