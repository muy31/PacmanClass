import json

alpha = 0.1
discount = 0.5

#Define map
allStates=[]
for i in range(1,4):
    for j in range(1,6):
            allStates.append((i,j))

actiontoNumber = {'U':0, 'D':1, 'L':2, 'R':3}

#Define paths (trials)
path1 = [(2,1), (1,1), (1,2), (1,3), (1,4), (2,4), (2,5)]
path1Actions = ['D', 'R', 'R', 'R', 'U', 'R']

path2 = [(2,1), (2,2), (3,2), (3,3), (2,3), (2,4), (2,5)]
path2Actions = ['R', 'U', 'R', 'D', 'R', 'R']

path3 = [(2,1), (3,1), (3,2), (3,3), (3,4), (2,4), (2,5)]
path3Actions = ['U', 'R', 'R', 'R', 'D', 'R']

#Define values
values = {}
for cd in allStates:
    values[cd] = [0, 0, 0, 0] #Order is U, D, L, R

#Define rewards
rewards = {}
for cd in allStates:
    if cd == (3,2):
        rewards[cd] = 2
    elif cd == (2,5):
        rewards[cd] = 10
    else:
        rewards[cd] = 0

def doTrial(path, pActions):
    for index in range(1, len(path) + 1):
        prevLoc = path[index - 1]
        
        if(index < len(path)):
            a = actiontoNumber[pActions[index - 1]]
            loc = path[index]
            values[prevLoc][a] = values[prevLoc][a] + alpha*(rewards[prevLoc] + discount* max(values[loc]) - values[prevLoc][a])
        else:
            #Terminal
            for a in range(0,4):
                values[prevLoc][a] = values[prevLoc][a] + alpha*(rewards[prevLoc] - values[prevLoc][a])

doTrial(path1, path1Actions)
print(values)
print()
doTrial(path2, path2Actions)
print(values)
print()
doTrial(path3, path3Actions)
print(values)
print()