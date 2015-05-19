k = int(input())
dictionary = []
#testdictionary = []

for i in range(0,k):
    word = input()
    dictionary.append(word)
    #simpleword = set(word)
    #testdictionary.append(simpleword)

N = int(input())

#mylist = [0,1,2,3]
#print(mylist[-1])

def compatible(swipe,testword):
    #print( 'Comparing testword: ' +str(testword)+' with swipe: '+str(swipe))
    for i in testword:
            if i not in swipe:
                #print(str(i)+' in the testword was not found in swipe')
                return False
    #print('compatible')
    return True

    
for i in range(0,N):
    swipe = input()
    found = False
    for i in range(0,len(dictionary)):
        #print('did this')
        testword = dictionary[i]
        firstletter = dictionary[i][0]
        lastletter = dictionary[i][-1]
        if swipe[0] != firstletter:
            #print('first letter didnt match')
            continue
        if swipe[-1] != lastletter:
            #print('last letter didnt match')
            continue
        if compatible(swipe,testword):
            print(dictionary[i])
            found = True
            break
    if found == False:
        print('?')
