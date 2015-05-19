import math

N = int(input())

def x(y,a,b):
    ans = a + b*y
    ans = ans*math.sin(2*math.pi*y)
    ans = (1-ans)*math.exp(-y*y)
    return ans


volume = []
for i in range(0,N):
    volume.append(0)
    #print(volume)
    values = input()
    values = values.split()
    a = float(values[0])
    b = float(values[1])
    h = float(values[2])
    #print(a)
    #print(b)
    #print(h)
    dx = h / 10000
    y = 0.5*dx
    #print('Y is : '+str(y)+' H is :'+str(h))
    while y < h:
        fy = x(y,a,b)
        ring = dx * fy*fy * math.pi
        volume[i] += ring
        #print(volume)
        y += dx

#print(volume)    

maxindex = 0
for i in range(0,len(volume)):
    if volume[i]>volume[maxindex]:
        maxindex = i
        
print(maxindex+1)