with open('a.txt') as f:
    lines = f.readlines()
    lines = [line.rstrip() for line in lines]
lines=lines[11:]


states=[]
actions=[]

for i in range(len(lines)):
    row=lines[i].split(' ')
    row=row[1:]
    temp=row
    if (row[0].isdigit() &len(row)>27):
        temp.pop(27)
        actions.append(row[27])
        states.append(temp)
    