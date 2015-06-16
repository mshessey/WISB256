import math
import numpy as np
import scipy
from scipy import integrate
#help(np)


class Lorentz:
    """ Butterflies are pretty"""
    def __init__(self,initstate,sig = 10,rho = 28,bet = 8/3):
        self.initstate = initstate
        self.sig = sig
        self.rho = rho
        self.bet = bet
        print("creating lorentz in state: "+str(initstate)+"sig: "+str(sig)+" rho: "+str(rho)+" bet: "+str(bet))
        
    def fdot(self,state,t):
        x = state[0]
        y = state[1]
        z = state[2]
        f0 = self.sig*(y-x)
        f1 = x*(self.rho - z)-y
        f2 = x*y-self.bet*z
        return [f0,f1,f2]
        
    
    def solve(self,T,dt):
        #solve on interval 0,T return two dimensional array. For each t, return array.
        ## first make dt array
        length = int(T/dt)+1
        timepoint = [0]*length
        for i in range(0,length):
            timepoint[i] = i*dt
        return scipy.integrate.odeint(self.fdot,self.initstate,timepoint)
        
    
            

