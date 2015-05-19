N = int(input())

verf = 0

for i in range(0,N):
    line = input()
    for i in line:
        if i == '#':
            verf += 5

print('Om de hekjes in dit weiland te verven heb je '+str(verf)+' liter verf nodig')
    