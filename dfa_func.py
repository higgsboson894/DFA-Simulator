a=[]
states=[]
def add_states():
    t=int(input('Enter number of states: '))
    for i in range(t):
        state=int(input('Enter state no: 0 is initial and last is final'))
        states.append(state)
    return states
def add_transitions(states,alphabet):
    transition=[]
    ch=0
    while ch<len(states):
        t=[]
        for i in alphabet:
            print("Enter state for alphabet",i,"from state ",ch)
            k=int(input())
            t.append(k)
        transition.append(t)
        ch=ch+1
    return transition
def transform(s,a):
    t=[]
    for i in s:
        t.append(a.index(int(i)))
    return t
def dfa(transition,alphabet,states,sequence):
    state=states[0]
    seq=transform(sequence,alphabet)
    for i in seq:
        state=transition[state][i]
        print("state is ",state)
    return state==states[len(states)-1]
        
 
    
    
            
        
    
     
    
    
    

