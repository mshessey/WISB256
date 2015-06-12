import lorentz
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


L1 = lorentz.Lorentz([-1,1,0])
u1 = L1.solve(50,0.1)
print(u1[0,0])

fig = plt.figure()
ax = fig.gca(projection='3d')

xs = u1[:,0]
ys = u1[:,1] 
zs = u1[:,2]
ax.plot(xs, ys, zs)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor")

plt.show()