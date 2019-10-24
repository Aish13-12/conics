import numpy as np
import matplotlib.pyplot as plt
import math

a=3
b=2
n=9
an=a/(2**(n-1))
print(an)
bn=((3**(1/2)/2)**(n-1))*b
print(bn)

len=100
theta=np.linspace(0,2*np.pi,len)
y_n = np.zeros((2,len))
O=np.array([0,0])

if(an>bn):
	e_n=(1-bn**2/an**2)**(1/2)
	l_n=2*(bn**2)/an
	print(l_n)
	y_n[0,:] = an*np.cos(theta)
	y_n[1,:] = bn*np.sin(theta)
	F_n1=np.array([an*e_n,0])
	F_n2=-F_n1
	plt.plot(y_n[0,:],y_n[1,:],label='E\N{SUBSCRIPT NINE}')

	plt.plot(O[0], O[1], 'o')
	plt.text(O[0] * (1 - 0.1), O[1] * (1 + 0.1) , 'O')
	plt.plot(F_n1[0], F_n1[1], 'o')
	
	plt.plot(F_n1[0], F_n1[1], 'o')
	plt.text(F_n1[0] * (1 - 0.1), F_n1[1] * (1 + 0.1) , 'F\N{SUBSCRIPT ONE}')
	
	plt.plot(F_n2[0], F_n2[1], 'o')
	plt.text(F_n2[0] * (1 - 0.1), F_n2[1] * (1 + 0.1) , 'F\N{SUBSCRIPT TWO}')
	

  		
if(bn>an):
	e_n=(1-an**2/bn**2)**(1/2)
	l_n=2*(an**2)/bn
	print(l_n)
	y_n[0,:] = an*np.cos(theta)
	y_n[1,:] = bn*np.sin(theta)
	F_n1=np.array([0,bn*e_n])
	F_n2=-F_n1
	plt.plot(y_n[0,:],y_n[1,:],label='E\N{SUBSCRIPT NINE}')

	plt.plot(O[0], O[1], 'o')
	plt.text(O[0] * (1 - 0.1), O[1] * (1 + 0.1) , 'O')
	plt.plot(F_n1[0], F_n1[1], 'o')
	
	plt.plot(F_n1[0], F_n1[1], 'o')
	plt.text(F_n1[0] * (1 - 0.1), F_n1[1] * (1 + 0.1) , 'F\N{SUBSCRIPT ONE}')
	
	plt.plot(F_n2[0], F_n2[1], 'o')
	plt.text(F_n2[0] * (1 - 0.1), F_n2[1] * (1 + 0.1) , 'F\N{SUBSCRIPT TWO}')
	
	

if(l_n==1/6):
	print("Length of latus rectum is 1/6")
	
else:
	print("Length of latus rectum is " +str(l_n)	)	
	





plt.axis('equal')

plt.xlabel('$x$');plt.ylabel('$y$')

plt.legend(loc='best')

plt.grid()
plt.show()


	
	



