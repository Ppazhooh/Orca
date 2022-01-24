import pandas as pd
import numpy as np

with open('b.txt') as f:
    lines = f.readlines()
    lines = [line.rstrip() for line in lines]
#lines=lines[11:]



states=[]
actions=[]

for i in range(len(lines)):
    row=lines[i].split(' ')
    row=row[1:]
    temp=row
    if (len(row)>27):
        if(row[0].isdigit()):
            actions.append(row[27])
            temp.pop(27)
            states.append(temp)


    
states=np.array(states)
actions=np.array(actions)

numpy_dict = {
        'actions': actions,
        'obs': states,
        # 'rewards': rewards,
        # 'episode_returns': episode_returns,
        # 'episode_starts': episode_starts
    }


np.savez("hi", **numpy_dict)

