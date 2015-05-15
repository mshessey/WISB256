def hasroot(f,a,b):
    if f(a) > 0:
        if f(b) < 0:
            return True
    elif f(a) < 0:
        if f(b) > 0:
            return True
    else:
        return False

def findroot(f,a,b,epsilon):
    print('Looking for root in ]'+str(a)+','+str(b)+'[')
    w = 0.5*(a+b)
    if abs(a-b) < epsilon:
        print('Foundroot (by squeeze) at: '+str(w))
        return w
    if abs(f(w))<0.0001:
        print('Foundroot (by direct) at: '+str(w))
        return w
    elif hasroot(f,a,w):
        findroot(f,a,w,epsilon)
    elif hasroot(f,w,b):
        findroot(f,w,b,epsilon)
    else:
        print('No roots in interval: ]'+str(a)+','+str(b)+'[')
        print('Returning -999')
        return -999
        
