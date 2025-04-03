def solution(picks, minerals):
    
    minerals = [minerals[x:x+5] for x in range(0,(min(sum(picks)*5,len(minerals))),5)]    
    work = {0:{"d":1,"i":1,"s":1},1:{"d":5,"i":1,"s":1},2:{"d":25,"i":5,"s":1}}
    answer = 0
    pick = [0]*picks[0]+[1]*picks[1]+[2]*picks[2]
    
    for i in range(len(minerals)):
        temp = 0
        for j in minerals[i]:
            temp += 1 if j[0] == "s" else 5 if j[0] == "i" else 25
        minerals[i]+=[temp]
    
    minerals.sort(key = lambda x: -x[-1])
    
    for i in minerals:
        if len(pick) == 0:
            break
        for j in i[:-1]:
            answer+=work[pick[0]][j[0]]
        del pick[0]
        
    return answer