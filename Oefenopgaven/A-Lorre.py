while True:
    lines = input('How many lines? ')
    try:
        lines = int(lines)
        break
    except:
        print('Must me int!')

for n in range (0,lines):
    while True:
        words = input('Say something ')
        try:
            str(words)
            break
        except:
            print('Must be a string')
    length = 1
    for s in words:
        if s == ' ':
            length +=1
        
    if length > 4:
        response = 'Crackers!'
    else:
        response = words+' krAh!'
    print(response)