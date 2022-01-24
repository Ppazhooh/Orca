import numpy as np
data=np.load('expert_cartpole.npz')
obs=data['obs']
print(type(data))