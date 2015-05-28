from Vector import Vector

vec1 = Vector(3,[1,0,3])
vec2 = Vector(3,[0,1,3])


print(vec1.norm())

answer = vec1.lincomb(vec2,3,16)
inn = vec1.inner(vec2)

print(answer)
print('--')
print(inn)