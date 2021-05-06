#
#
import numpy as np

# Creo un array de 1x1
alpha = np.array([5])
print('alpha scalar is of dim %d' %(alpha.shape))

# Creo un array/matriz de 1x6
x = np.array([1,1,2,3,5,8])
print('x scalar is of dim %d' %(x.shape))

x2 = np.array([[1],[1],[2],[3],[5]])
print('x2: ' + str(x2.shape))

