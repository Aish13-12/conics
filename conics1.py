import numpy as np
import math
import matplotlib.pyplot as plt
from numpy import linalg as LA
from coeffs import *

fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')

len = 50
o=np.vstack([0,0])
y_11 = np.linspace(-1,1,len)
y_21= np.power((3**0.5)*y_11,2)

y_1 = np.vstack((y_11,y_21))


y_22 = np.linspace(-1,1,len)
y_21 = np.power((3**0.5)*y_22,2)

y_2= np.vstack((y_21,y_22))


plt.plot(y_1[0,:],y_1[1,:],label='Parabola_1')
plt.plot(y_2[0,:],y_2[1,:],label='Parabola_2')
plt.plot(o[0], o[1], 'o')
plt.text(o[0] * (1 + 0.5), o[1] * (1 - 0.1) , 'O')

ax.plot()
plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best');plt.grid()
plt.show()

