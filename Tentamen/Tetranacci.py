g0 = 0
g1 = 0
g2 = 0
g3 = 1

N =  int(input())

for i in range(0,N):
    gnext = g3+g2+g1+g0
    g0 = g1
    g1 = g2
    g2 = g3
    g3 = gnext


print(g0)
