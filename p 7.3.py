import numpy as np
import sympy as sp
x = sp.Symbol("x")
A=np.array([[1,1],[1,0]])
e1=np.array([[1],[1/x]])
e2=np.array([[1],[-x]])
Ae1=np.dot(A,e1)
print("Ae1:",Ae1)
#x-1=1/x
if Ae1[0]==1+1/x:
    Ae1[0]=x
print("landa1 is:",Ae1[0])
Ae2=np.dot(A,e2)
if Ae2[0]==1-x:
    Ae2[0]=-1/x
print("Ae2:",Ae2)
print("landa2 is:",Ae2[0])

