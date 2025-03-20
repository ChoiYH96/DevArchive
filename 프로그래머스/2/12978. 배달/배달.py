def solution(N, road, K):
    answer = 0
    cost = [[float('inf') if y != x else 0 for y in range(N)] for x in range(N)]

    for i in road:
        cost[i[0]-1][i[1]-1] = min(cost[i[0]-1][i[1]-1],i[2])
        cost[i[1]-1][i[0]-1] = min(cost[i[0]-1][i[1]-1],i[2])

    for i in cost:
        print(i)
    return -1