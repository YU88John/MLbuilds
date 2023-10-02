import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(1,5,11)
y = x ** 2
#Traditional method
plt.plot(x,y,'b')
plt.title('Traditional')
plt.show()

#subplotting(two plots)
plt.subplot(1,2,1)
plt.plot(x,y,'r')
plt.subplot(1,2,1)
plt.plot(y,x,'b')
plt.subplot(2,2,2) #(rows,columns, which plot must between 1 and 2 or equal)
plt.plot(x,y,'g')

#Object oriented
fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.7])
axes1.plot(x,y)
axes1.set_title('Obj Oriented')
axes1.set_xlabel('X')
axes1.set_ylabel('Y')

axes2 = fig.add_axes([0.3,0.4,0.3,0.3])
axes2.plot(y,x)
axes2.set_title('Obj Oriented-2')
axes2.set_xlabel('Y')
axes2.set_ylabel('X')
plt.show()