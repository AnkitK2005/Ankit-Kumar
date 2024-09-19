#numpy advanced
import numpy as np
a=np.array([1,2,3])
b=np.array([4,5,6])
print(type(a))
print(a.shape)
print(type(b))
print(b.shape)
print(a[0],a[1],a[2])
a[0]=5
print(a)
b=np.array([[1,2,3],[4,5,6]])
print(b.shape)
print(b[0,0],b[0,1],b[1,0])


import numpy as np
a=np.zeros((2,2))
print(a)
b=np.ones((1,2))
print(b)
c=np.full((2,2),7)
print(c)
d=np.eye(2)
print(d)
e=np.random.random((2,2))
print(e)


import numpy as np
np.linspace(2.0,3.0,num=5)
np.linspace(2.0,3.0,num=5, retstep=True)
np.linspace(2.0,3.0,num=5, endpoint=False)


import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print((a))
b=a[:2,1:3]
print((b))
print(a[0,1])
print(a[:,:])
print(a[:2,1:3])
print(a[0:2,1:2])
print(a[2:3,0:2])
print(a[:2,1:])
print(a[-3:-1,-2:-1])
print(a[-2:1,1:3])

import numpy as np
a=np.array([[1,2],[3,4],[5,6]])
print(a[[0,1,2],[0,1,0]])
print(np.array([a[0,0],a[1,1],a[2,0]]))
print(a[[0,0],[1,1]])
print(np.array([a[0,1],a[0,1]]))


import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(a)
b=np.array([0,2,0,1])
print(b)
print(a[np.arange(4),b])
a[np.arange(4),b]+=10
print(a)


import numpy as np
a=np.array([[1,2],[3,4],[5,6]])
bool_idx=(a>2)
print(bool_idx)
print(a[bool_idx])
print(a[a>2])

import numpy as np
x=np.array([1,2])
print(x.dtype)
x=np.array([1.0,2.0])
print(x.dtype)
x=np.array([1,2],dtype=np.int64)
print(x.dtype)


import numpy as np
a=np.array([[1,2],[3,4]])
eigenvalues,eigenvectors=np.linalg.eig(a)
print("eigenvalues:")
print(eigenvalues)
print("\n eigenvectors:")
print(eigenvectors)

import numpy as np
x=np.array([[1,2],[3,4]],dtype=np.float64)
y=np.array([[5,6],[7,8]],dtype=np.float64)
print(x+y)
print(np.add(x,y))
print(x-y)
print(np.subtract(x,y))
print(np.divide(x,y))
print(x/y)
print(x*y)
print(np.multiply(x,y))
print(np.sqrt(x))

import numpy as np
x=np.array([[1,2],[3,4]])
print(x)
print(x.T)
v=np.array([1,2,3])
print(v)
print(v.T)


