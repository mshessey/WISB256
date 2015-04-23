name = input('What is your name?')
print('Hello ' + name )
finished = False
while(not finished):
    x = input('How many times?')
    try:
        x = int(x)
        print(str(x) + ' x Hello, ' + name)
        finished = True
    except:
        print('Bad input, try again')
    
    
    
