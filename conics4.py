import numpy as np
import matplotlib.pyplot as plt
import math


a=9
b=-18
c=5
e_1=(-b+(b**2-4*a*c)**(1/2))*(1/(2*a))
print(e_1)
e_2=(-b-(b**2-4*a*c)**(1/2))*(1/(2*a))
print(e_2)

S=np.array([5,0])
l=(S@S.T-9)/np.linalg.norm(S)
l=abs(l)
print(l)

if e_1>1:
	a=(l*e_1)/(e_1**2-1)
	print(a)
	b=a*((e_1**2-1)**(1/2))
	p=a**2-b**2
	print(p)

if e_2>1:
	a=(l*e_2)/(e_2**2-1)
	print(a)
	b=a*((e_2**2-1)**(1/2))
	p=a**2-b**2
	print(p)

len=10
theta=np.linspace(0,2*np.pi,len)
y = np.zeros((2,len))
y[0,:] = a*np.cosh(theta)
y[1,:] = b*np.sinh(theta)


plt.plot(y[0,:],y[1,:],label='Hyperbola')

plt.axis('equal')

plt.xlabel('$x$');plt.ylabel('$y$')

plt.legend(loc='best')

plt.grid()
plt.show()

