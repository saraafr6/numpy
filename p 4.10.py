#compute the matrix products a) AB, b) AA, c) BA, and d) BB

import numpy as np
a=np.array([[1,1,1],[0,4,2],[3,1,0]])
b=([[3,1],[2,0],[1,1]])


#a)
print("ab is:\n",np.dot(a,b))

#b)
print("aa is:\n",np.dot(a,a))

#c)
print("ba ----> error")

#d)
print("bb -----> error")
