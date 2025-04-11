import heapq

def solution(n, costs):
    
    answer = 0
    visited = {0}
    node = {x:[] for x in range(n)}
    
    for i in costs:
        node[i[0]] += [(i[2],i[1])]
        node[i[1]] += [(i[2],i[0])]
    
    heap = [(x[0],x[1],0) for x in node[0]]
    heapq.heapify(heap)
    
    while len(visited) < n:
        cost, end, start = heapq.heappop(heap)
        if end not in visited:
            answer+=cost
            visited.add(end)
            for i in node[end]:
                heapq.heappush(heap,(i[0],i[1],end))
    return answer
