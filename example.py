import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('data')
x = data[:,0]
y = data[:,1]

print(x)
print(y)

y2 = y*y


#x = np.linspace(0, 10, num=101)
#y = np.sqrt(x)
#print(x)
fig, ax = plt.subplots()

ax.plot(x, y , '-', linewidth=2)
ax.plot(x, y2 , '-', linewidth=2)

ax.set_xlabel(r"Mass [M$_\odot$]")
ax.set_ylabel("redshift")
#dashes = [10, 5, 100, 5] # 10 points on, 5 off, 100 on, 5 off
#line.set_dashes(dashes)

#plt.show()
plt.savefig("example.ps")
