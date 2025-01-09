def solution(n, results):
    match = {x:[[],[]] for x in range(1,n+1)}
    answer = [ 0 for _ in range(n)]
    
    for i in results:
        match[i[0]][0] += [i[1]]
        match[i[1]][1] += [i[0]]
        
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if k == i or k == j or i == j:
                    continue
                else:
                    if k in match[i][0] and j in match[k][0]:
                        match[i][0] = list(set(match[i][0]+[j]))
                    elif k in match[i][1] and j in match[k][1]:
                        match[i][1] = list(set(match[i][1]+[j]))

    return [len(x[0])+len(x[1]) for x in match.values()].count(n-1)