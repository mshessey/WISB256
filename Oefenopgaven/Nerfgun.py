import math

Vk = float(input())
V2 = Vk*Vk
A = float(input())
S = float(input())

alpha = 0.5 * math.asin(A/V2*S)
answer = "{0:.2f}".format(alpha)
print(str(answer))

