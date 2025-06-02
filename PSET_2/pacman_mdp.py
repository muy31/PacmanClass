discount = 0.5

#Define all states
all_states=[]
for i in range(1,6):
    all_states.append(i)
all_states.append('Out')

#State of all actions
allActions = ('R', 'Fly')

#Define rewards for all states
rewards = {}
for i in allActions:
    if i == 'R':
        rewards[i] = 10
    elif i == 'Fly':
        rewards[i] = 20



#Dictionary of possible actions. Every state can undergo every action except for the terminal states
actions = {
    1:allActions,
    2:allActions,
    3:allActions,
    4:allActions,
    5:('Fly',)
}


#Define initial value function 
V={}
for s in all_states:
    if s in actions.keys():
        V[s] = 0
V['Out'] = 0

def doMove(s, a):
    if a == 'R':
        nxt = s + 1
    elif a == 'Fly':
        nxt = 'Out'
    if nxt not in all_states:
        nxt = 'Out'
    return nxt

def qValue(s, a, Va):
    if a == 'R':
        nxt = doMove(s, 'R')
        return rewards[a] + discount*Va[nxt]

    elif a == 'Fly':
        nxt = doMove(s, 'Fly')
        return rewards[a] + discount*Va[nxt] 

    return None


flyPolicy = {
    1:'Fly',
    2:'Fly',
    3:'Fly',
    4:'Fly',
    5:'Fly',
}

flyat4Policy = {
    1:'R',
    2:'R',
    3:'R',
    4:'Fly',
    5:'Fly',
}

flyat5Policy = {
    1:'R',
    2:'R',
    3:'R',
    4:'R',
    5:'Fly',
}

VFpolicy = V.copy()
V4policy = V.copy()
V5policy = V.copy()

print(qValue(3, 'R', V))

def printOutVals(vals):
        st = ""
        for i in range(6):
            if i in all_states:
               st += f"{vals[i] :0.2f} "
            else:
               st += "##### "
        print(st)

#Finding optimal policy
for batchCount in range(0, 10):
    Vnew = {}
    print("Iteration: " + str(batchCount + 1) + "\n")
    for s in actions.keys():
        values = []
        for a in actions[s]:
            val = qValue(s, a, V)
            values.append(val)
            print(a)
        print(str(s) +" R, Fly: " + str(values))
        Vnew[s] = max(values)
    V = Vnew.copy()
    V['Out'] = 0
    printOutVals(V)
    print()

def iteratePolicy(policy, values):
    print("Policy-Based Evaluation Iteration: 0")
    printOutVals(values)
    for batchCount in range(0, 10):
        p2 = {}
        #print("Policy-Based Evaluation Iteration: " + str(batchCount + 1) + "\n")
        for s in actions.keys():
            policyBasedValue = qValue(s, policy[s], values)
            p2[s] = policyBasedValue
        values = p2.copy()
        values['Out'] = 0
    printOutVals(values)
    print()


iteratePolicy(flyPolicy, VFpolicy)
iteratePolicy(flyat4Policy, V4policy)
iteratePolicy(flyat5Policy, V5policy)