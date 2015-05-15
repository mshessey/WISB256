def hasroot(f,a,b):
    if f(a) > 0:
        if f(b) < 0:
            return True
    elif f(a) < 0:
        if f(b) > 0:
            return True
    else:
        return False

def combinterval(f,a,b,teeth):
    print('Combing with '+str(teeth)+' teeth...')
    dx = abs(b-a)/teeth
    if f(a) < 0:
        x = a
        for i in range(1,teeth):
            x += dx
            if f(x) > 0:
                return x
    elif f(a) <0:
        x = a
        for i in range(1,teeth):
            x += dx
            if f(x) < 0:
                return x
    else:
        print("Combing didn't find candidates for root")
        return False
    
def findroot(f,a,b,epsilon):
    #print('Looking for root in ]'+str(a)+','+str(b)+'[')
    w = 0.5*(a+b)
    if abs(a-b) < epsilon:
        print('Foundroot (by squeeze) at: '+str(w))
        w = float(w)
        #print(type(w))
        return w
    if abs(f(w))<0.0001:
        print('Foundroot (by direct) at: '+str(w))
        w = float(w)
        #print(type(w))
        return w
    elif hasroot(f,a,w):
        w = findroot(f,a,w,epsilon)
    elif hasroot(f,w,b):
        w = findroot(f,w,b,epsilon)
    else:
        print('Findroot failed to find root on interval.]'+str(a)+','+str(b)+'[.')
        teeth = 10
        
        while True:
            myvar = combinterval(f,a,b,teeth)
            if  myvar == False:
                teeth = teeth*10
                gap = abs(a-b) / teeth
                if gap < epsilon: # Dont do the next level of precision
                    return False
            else:
                print('Combing worked, returning: '+str(myvar))
                return myvar
            
        print('Returning FALSE')
        return False
    return w
        


def findallrootinner(f,a,b,epsilon,outlist):
    root = findroot(f,a,b,epsilon)
    if root == False:
        print("Finished Looking for roots")
        print(outlist)
        #print('The END!')
        return outlist
    else:
        print('Passed root:'+ str(root))
        outlist.append(root)
        #print(outlist)
        #print('Root: '+str(root))
        #print(type(root))
        print('X variable temp value before root devision: '+str(x))
        print('abs(x-root)'+str(abs(x-root)))
        g = lambda x: f(x)/(x-root)
        findallrootinner(g,a,b,epsilon,outlist)
        return outlist
        
def findAllroots(f,a,b,epsilon):
    outlist = []
    outlist = findallrootinner(f,a,b,epsilon,outlist)
    return outlist