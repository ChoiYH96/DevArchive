from collections import deque

def solution(n, edge):
    
    temp = deque([1])
    node = {x:[] for x in range(1,n+1)}
    visited = [False]+[True]*(n-1)
    
    for i in edge:
        node[i[0]] += [i[1]]
        node[i[1]] += [i[0]]
    
    while temp:
        cnt = 0
        for i in temp.copy():
            visited[i-1] = False
            cnt+=1
            for j in node[i]:
                if visited[j-1]:
                    visited[j-1] = False
                    temp.append(j)
            temp.popleft()

    return cnt