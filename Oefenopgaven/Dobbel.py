# template: position[Top,Achter,Beneden,Voor,Links,Rechts]
startposition = [6,3,1,4,2,5]

def omhoog(position):
    newposition = [0,0,0,0,0,0]
    newposition[0] = position[3]
    newposition[1] = position[0]
    newposition[2] = position[1]
    newposition[3] = position[2]
    newposition[4] = position[4]
    newposition[5] = position[5]
    return newposition
    
def omlaag(position):
    newposition = [0,0,0,0,0,0]
    newposition[0] = position[1]
    newposition[1] = position[2]
    newposition[2] = position[3]
    newposition[3] = position[0]
    newposition[4] = position[4]
    newposition[5] = position[5]
    return newposition
    
def links(position):
    newposition = [0,0,0,0,0,0]
    newposition[0] = position[5]
    newposition[2] = position[4]
    newposition[4] = position[0]
    newposition[5] = position[2]
    
    newposition[1] = position[1]
    newposition[3] = position[3]
    return newposition
    
def rechts(position):
    newposition = [0,0,0,0,0,0]
    newposition[0] = position[4]
    newposition[2] = position[5]
    newposition[4] = position[2]
    newposition[5] = position[0]
    
    newposition[1] = position[1]
    newposition[3] = position[3]
    return newposition
    
rollen = int(input())
dieposition = startposition
for i in range(0,rollen):
    move = input()
    if move == 'omhoog':
        dieposition = omhoog(dieposition)
    elif move == 'omlaag':
        dieposition = omlaag(dieposition)
    elif move == 'links':
        dieposition = links(dieposition)
    elif move == 'rechts':
        dieposition = rechts(dieposition)
    else:
        print('Error: Input: '+str(move)+' did not match option')
        
print(str(dieposition[0]))