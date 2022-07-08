import numpy as np
#(a)
m1 = np.arange(20).reshape(4, 5)
print ( m1.ndim )
print(m1)
#(b)
m2 = m1[:, ::-1]
print (m2)
#(c)
m3 = m1[::-1]
print (m3)
#(d)
m4 = m1 [1:3,1:4:]
print (m4)
