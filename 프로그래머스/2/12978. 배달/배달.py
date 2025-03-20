def solution(N, road, K):
    answer = 0
    cost = [[float('inf') if y != x else 0 for y in range(N)] for x in range(N)]

    for i in road:
        cost[i[0]-1][i[1]-1] = min(cost[i[0]-1][i[1]-1],i[2])
        cost[i[1]-1][i[0]-1] = min(cost[i[0]-1][i[1]-1],i[2])
    
    node = [x for x in range(N) if 0 < cost[0][x] < float('inf')]
    
    while len(node) != 0:
        
        for i in range(N):
            if cost[0][i] > cost[0][node[0]]+cost[node[0]][i]:
                cost[0][i] = cost[0][node[0]]+cost[node[0]][i]
                node += [i]
        del node[0]

    return len([x for x in cost[0] if x <= K])