def recusivecount(n,myname):
    if n >= 1:
        print(n)
        recusivecount(n-1,myname)
        return n
    elif n == 0:
        print(str(n)+' Time to cheer '+str(myname))
        return n
        
recusivecount(10,'Max')
print(type(recusivecount(10,'max')))