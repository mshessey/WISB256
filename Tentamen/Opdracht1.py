taal = input()
cijfer = False
try:
    int(taal)
    cijfer = True
    taal = int(taal)
except:
    taal = str(taal)
    cijfer = False
    
if cijfer:
    words = 'Ug'
    for i in range(1,taal):
        words = words+' ug'
    words = words+' !'
    print(words)
    
else:
    taal = taal.split()
    words = len(taal)
    print(words)