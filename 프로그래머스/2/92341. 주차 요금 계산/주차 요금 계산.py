def solution(fees, records):
    
    records = sorted([x.split() for x in records], key = lambda x : (x[1],x[0]))
    history = {x[1]: [] for x in records if x[2] == "IN"}
    time = []
    
    for i in records:
        history[i[1]] += [i[0]]
    
    for i in history:
        if len(history[i]) % 2 != 0:
            history[i]+=["23:59"]
    
    for i in history:
        temp = 0
        for j in range(1,len(history[i]),2):
            entry, out = list(map(int, history[i][j-1].split(":"))), list(map(int, history[i][j].split(":")))
            temp += (out[0]-entry[0])*60 + out[1]-entry[1]
        time+=[temp]
        
    return [fees[1] if x <= fees[0] else fees[1] + (-(-(x-fees[0])//fees[2]))*fees[3] for x in time]