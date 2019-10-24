import numpy as np
from conics6 import*

if(an>bn):
	F_n1=np.array([an*e_n,0])
	O=np.array([0,0])
	D=F_n1-O
	d=np.linalg.norm(D)
	print(d)
	
if(bn>an):
	F_n1=np.array([0,bn*e_n])
	O=np.array([0,0])
	D=F_n1-O
	d=np.linalg.norm(D)
	print(d)	
	
if(d==(5**(1/2))/32):
	print(True)
	
else:
	print(False)	
	

