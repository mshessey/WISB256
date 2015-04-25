name = input('What is your name? ')
finished = False
while(not finished):
    x = input('How many greetings? ')
    try:
        x = int(x)
        print(str(x) + ' x Hello, ' + name + '!')
        finished = True
    except:
        print('Bad input, try again')
    
    
    
