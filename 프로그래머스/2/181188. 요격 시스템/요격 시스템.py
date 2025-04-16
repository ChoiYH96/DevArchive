def solution(targets):
    
    targets = sorted(targets, key = lambda x: (x[0],(x[1]-x[0])))
    temp = targets[0][1]
    answer = 1
    
    for i in targets[1:]:
        if i[0] >= temp:
            answer+=1
            temp = i[1]
        else:
            temp = min(temp,i[1])
            
    return answer