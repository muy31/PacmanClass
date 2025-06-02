
discount = 0.8
primeProb = 0.8
sideProb = 0.1

#Define all states
all_states=[]
for i in range(5):
    for j in range(5):
            all_states.append((i,j))

#Remove the walls (inaccessible states)
all_states.remove((0,0))
all_states.remove((1,0))
all_states.remove((1,2))
all_states.remove((1,3))
all_states.remove((2,3))


#Define rewards for all states
rewards = {}
for i in all_states:
    if i == (2,0):
        rewards[i] = -1
    elif i == (1,1):
        rewards[i] = 1
    elif i == (2,2):
        rewards[i] = -1
    else:
        rewards[i] = -0.01


allActions = ('U', 'D', 'L', 'R')
#Dictionary of possible actions. Every state can undergo every action except for the terminal states
actions = {cd:allActions for cd in all_states}
del actions[(2,0)]
del actions[(1,1)]
del actions[(2,2)]

#Define initial value function 
V={}
for s in all_states:
    if s in actions.keys():
        V[s] = 0
    if s ==(2,2):
        V[s]=-1
    if s == (2,0):
        V[s]=-1
    if s == (1,1):
        V[s]=1

def doMove(s, a):
    if a == 'U':
        nxt = (s[0]-1, s[1])
    elif a == 'D':
        nxt = (s[0]+1, s[1])
    elif a == 'L':
        nxt = (s[0], s[1]-1)
    elif a == 'R':
        nxt = (s[0], s[1]+1)

    if nxt not in all_states:
        nxt = s
    return nxt

def qValue(s, a, Va):
    if a == 'U':
        nxtU = doMove(s, 'U')
        nxtL = doMove(s, 'L')
        nxtR = doMove(s, 'R')
        
        return primeProb * (rewards[s] + discount*Va[nxtU]) + sideProb * (rewards[s] + discount*Va[nxtL]) + sideProb*(rewards[s] + discount*Va[nxtR])

    elif a == 'D':
        nxtU = doMove(s, 'D')
        nxtL = doMove(s, 'L')
        nxtR = doMove(s, 'R')
        
        return primeProb * (rewards[s] + discount*Va[nxtU]) + sideProb * (rewards[s] + discount*Va[nxtL]) + sideProb*(rewards[s] + discount*Va[nxtR])
    elif a == 'L':
        nxtU = doMove(s, 'L')
        nxtL = doMove(s, 'U')
        nxtR = doMove(s, 'D')
        
        return primeProb * (rewards[s] + discount*Va[nxtU]) + sideProb * (rewards[s] + discount*Va[nxtL]) + sideProb*(rewards[s] + discount*Va[nxtR])
    elif a == 'R':
        nxtU = doMove(s, 'R')
        nxtL = doMove(s, 'U')
        nxtR = doMove(s, 'D')
        
        return primeProb * (rewards[s] + discount*Va[nxtU]) + sideProb * (rewards[s] + discount*Va[nxtL]) + sideProb*(rewards[s] + discount*Va[nxtR])
    return None


initPolicy = {
    (0,1):'L',
    (0,2):'D',
    (0,3):'R',
    (0,4):'L',
    (1,4):'R',
    (2,1):'R',
    (2,4):'U',
    (3,0):'R',
    (3,1):'U',
    (3,2):'D',
    (3,3):'U',
    (3,4):'R',
    (4,0):'L',
    (4,1):'U',
    (4,2):'R',
    (4,3):'U',
    (4,4):'U',
}

Vpolicy = V.copy()


def printOutVals(vals):
    for i in range(5):
        st = ""
        for j in range(5):
            if (i,j) in all_states:
               st += f"{vals[(i,j)] :0.3f} "
            else:
               st += "##### "
        print(st)


for batchCount in range(0, 5):
    Vnew = {}
    print("Iteration: " + str(batchCount + 1) + "\n")
    for s in actions.keys():
        values = []
        for a in actions[s]:
            val = qValue(s, a, V)
            values.append(val)
        print(str(s) +" U,D,L,R: " + str(values))
        Vnew[s] = max(values)
    V = Vnew.copy()
    V[(2,2)] = -1
    V[(2,0)] = -1
    V[(1,1)] = 1
    printOutVals(V)
    print()

print("Policy-Based Evaluation Iteration: 0")
printOutVals(Vpolicy)
print(rewards[(0,4)])
print(qValue((0,4), 'L', Vpolicy))

for batchCount in range(0, 5):
    Vp2 = {}
    print("Policy-Based Evaluation Iteration: " + str(batchCount + 1) + "\n")
    for s in actions.keys():
        policyBasedValue = qValue(s, initPolicy[s], Vpolicy)
        print(str(s) + " " + initPolicy[s] + " " + str(policyBasedValue))
        Vp2[s] = policyBasedValue
    Vpolicy = Vp2.copy()
    Vpolicy[(2,2)] = -1
    Vpolicy[(2,0)] = -1
    Vpolicy[(1,1)] = 1
    printOutVals(Vpolicy)
    print()


