line1 = input()
line2 = input()
line3 = input()

game = [line1,line2,line3]

def horwin(line):
    original = line[0]
    for i in line:
        if i != original:
            return 0 #no one
    return original


def vertwin(col):
    original=line1[col]
    for line in game:
        if line[col] != original:
            return 0
    return original
    
def downdiagwin():
    original = game[0][0]
    for i in range(1,3):
        if game[i][i] != original:
           # print('Tested: '+str(game[i][i])+' Against: '+str(original))
            return 0
    return original
    
def updiagwin():
    original = game[2][0]
    for i in range(1,3):
        if game[2-i][i] != original:
            return 0
    return original



def findwinner():
    ret = downdiagwin()
    if ret != 0:
            #print('downdiagwin')
            return ret
    ret = updiagwin()
    if ret != 0:
            #print('updiagwin')
            return ret
    for i in range (0,3):
        ret = horwin(game[i])
        if ret != 0:
           # print('horwin in line: '+str(i))
            return ret
        ret = vertwin(i)
        if ret != 0:
            #print('verwin in col: '+str(i))
            return ret
    return 0   

if findwinner()=='1':
    output = 'Player 1 Wins'
    
if findwinner()=='2':
    output = 'Player 2 Wins'
    
if findwinner()==0:
    output = 'No Winner'
print(output)