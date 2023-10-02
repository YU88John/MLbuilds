import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0,100)
y = x*2
z = x**2

fig = plt.figure()
#ax = fig.add_axes([0,0,1,1])
#ax.plot(x,y)
#ax2 = fig.add_axes([0.2,0.5,0.2,0.2])
#ax2.plot(x,y)

ax3 = fig.add_axes([0,0,1,1])
ax3.plot(x,z)
ax3.set_xlabel('X')
ax3.set_ylabel('Z')
ax4 = fig.add_axes([0.2,0.5,0.4,0.4])
ax4.plot(x,y)
ax4.set_xlabel('X')
ax4.set_ylabel('Y')
ax4.set_title('ZOOM')

figS,axes = plt.subplots(nrows=1, ncols=2, figsize=(9,3))
axes[0].plot(x,y, color='blue', lw=3, ls=':')  #marker 
axes[1].plot(x,z, color='red')
plt.show()


