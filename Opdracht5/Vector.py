import math

class Vector:
    length = 0
    def __init__(self,n,waarde=0):
        self.length = n
        if type(waarde)==list:
            self.element=waarde
        else:
            self.element = [waarde]*n

    def __str__(self):
        rets = ''
        for i in range(0,self.length):
            rets=rets+str(self.element[i])
            if i < self.length-1:
                rets=rets+'\n'
        return rets
    
    def scalar(self,a):
        retvec = Vector(self.length)
        for i in range(0,self.length):
            retvec.element[i]=self.element[i]*a
        return retvec
            
    def lincomb(self,other,a,b):
        retvec = Vector(self.length)
        tempvec1 = self.scalar(a)
        tempvec2 = other.scalar(b)
        for i in range(0,self.length):
            retvec.element[i] = tempvec1.element[i]+tempvec2.element[i]
        return retvec
        
    def inner(self,other):
        retfl = 0.
        for i in range(0,self.length):
            retfl = retfl + self.element[i]*other.element[i]
        return retfl
        
        
    def norm(self):
        retfl = self.inner(self)
        retfl = math.sqrt(retfl)
        return retfl
        
        """This is a dead parrot"""