import heapq as hq

def solution(n, roads, sources, destination):
    
    route = {x:[] for x in range(1,n+1)}
    temp = [-1 if x != destination-1 else 0 for x in range(n)]
    
    for i in roads:
        route[i[0]]+=[i[1]]
        route[i[1]]+=[i[0]]
        if destination in i:
            temp[(i[0] if i[0] != destination else i[1])-1] = 1

    cnt = [tuple([1,x]) for x in route[destination]]
    
    hq.heapify(cnt)
    while cnt:
        distance, node = hq.heappop(cnt)
        for i in [x for x in route[node] if temp[x-1] == -1]:
            temp[i-1] = distance + 1
            hq.heappush(cnt,(distance+1,i))

    return [temp[x-1] for x in sources]