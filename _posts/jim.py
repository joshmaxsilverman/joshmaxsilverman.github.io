import itertools
#generate binary states and sort by number of flipped tiles 
n=9
N=2**n
states_init = list(itertools.product([0, 1], repeat=n))
total =[]
for y in states_init:
    total.append(sum(y))
states= [x for _,x in sorted(zip(total,states_init))]
 
# function to generate all subsets of a given set
def powerset(items):
    combo = []
    for a in range(len(items) + 1):
        combo.append(list(itertools.combinations(items,a)))
    return combo
# function to determine move that results in highest probability subsequent state
def find_best_next_state(state_num, roll):
    unflipped_combos = powerset([d+1 for d,val in enumerate(states[state_num]) if val==0])
    s = -1
    p_max = 0
    for c in unflipped_combos:     
        for t in c:
            if sum(t) != roll:
                continue
            state_test = list(states[state_num])
            for e in list(t):
                state_test[e-1] = 1
            state_num_test = states.index(tuple(state_test))
            if prob[state_num_test] > p_max:
                p_max = prob[state_num_test]
                s = state_num_test                
    return s
# start at final state and work backward, determining if one or two die rolls is optimal
prob = [0]*N
die = [1]*N
prob[N-1] = 1
for i in range(N-2,-1,-1):
    p1 = p2 = 0
    for j in range(6):
        for k in range(6):
            s = find_best_next_state(i,j+k+2)
            if s != -1:
                p2 += prob[s] / 36
    for j in range(6):          
            s = find_best_next_state(i,j+1)
            if s != -1:
                p1 += prob[s] / 6           
    prob[i] = max(p1,p2) #forcing 2 rolls for 7/8/9 doesnt change answer
    die[i] += 1 * (p2 > p1)#keep track of which number of die rolls is optimal
print("Probablity of finishing: ", prob[0])