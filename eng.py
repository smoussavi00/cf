import cityflow
import json
import pprint
import numpy as np

eng = cityflow.Engine('cf3.json')


eng.next_step()



'''

mov = {}
int_roads = {}
f = open('33/rn3.json')

data = json.load(f)["intersections"]

for int in data:
    if not (int["point"]["x"] == 900 or int["point"]["x"] == -300 or int["point"]["y"] == 900 or int["point"]["y"] == -300):
        mov[f'{int["id"]}'] = []
        int_roads[f'{int["id"]}'] = []
        for rl in int["roadLinks"]:

            if rl["startRoad"] not in int_roads[f'{int["id"]}']:
                int_roads[f'{int["id"]}'].append(rl["startRoad"])
            if rl["endRoad"] not in int_roads[f'{int["id"]}']:
                int_roads[f'{int["id"]}'].append(rl["endRoad"])

            if(rl["type"] == 'go_straight'):
                mov[f'{int["id"]}'].append((rl["startRoad"],rl["endRoad"],1))
            elif(rl["type"]== 'turn_left'):
                mov[f'{int["id"]}'].append((rl["startRoad"],rl["endRoad"],0))


pr = {}
R = {}
st = {}
stprev = {}

Wdict = {}

W = np.ones((25,4))
for k,v in mov.items():
    Wdict[k] = W.copy()

a = {}
aprev = {}

B = 0
beta = 0.4
alpha = 0.05
step_size = 0.02
gamma=0.85

epsilon = 0.1



for i in range(3000):
    
    B = 0
    eng.next_step()

    if i % 30 == 0:

        x = eng.get_lane_vehicle_count()

        for k,v in mov.items():
                u = 0
                st[k] = np.zeros(25)
                st[k][u] = eng.get_tl_phase(k)
                u+=1
                for rd in int_roads[k]:
                    st[k][u] = x[f'{rd}_0']
                    u+=1
                    st[k][u] = x[f'{rd}_1']
                    u+=1
                    st[k][u] = x[f'{rd}_2']
                    u+=1

        for k,v in mov.items():
            y = np.random.rand(1)[0]
            if y < epsilon:
                a[k] = 2*np.random.randint(0,4)
            else:
                a[k] = 2*np.argmax(np.transpose(Wdict[k]) @ st[k])
            eng.set_tl_phase(k,a[k])


        #OBSERVE R and S' from A OF PREVIOUS ITERATION
        if(i > 0):
            for k,v in mov.items():
                pr[k] = [0,0]
                if k == 'intersection_2_2':
                    pr[k] = [0,1]
                for m in v:
                    pr[k][0] += x[f'{m[0]}_{m[2]}'] - x[f'{m[1]}_{m[2]}']
            for j in range(2):
                if(j == 0):
                    B += beta**(1-j)*(sum([v[0] for (k,v) in pr.items() if v[1] == j])/8)
                else:
                    B += beta**(1-j)*sum([v[0] for (k,v) in pr.items() if v[1] == j])

            for k,v in mov.items():
                R[k] = -pr[k][0]-(alpha*B)
                print(Wdict[k][:,(aprev[k]//2)])
                Wdict[k][:,(aprev[k]//2)] = Wdict[k][:,(aprev[k]//2)] + ( step_size * (R[k]+gamma*(np.max(np.transpose(Wdict[k]) @ st[k])) - (np.transpose(Wdict[k]) @ stprev[k])[(aprev[k]//2)]) ) * stprev[k]

        stprev = st.copy()
        aprev = a.copy()

pprint.pprint(Wdict['intersection_2_2'])
        
'''



