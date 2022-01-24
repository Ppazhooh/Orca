import numpy as np
data=np.load('hi.npz')
obs=data['obs']
print(type(data))
print(type(obs))