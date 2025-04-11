import heapq

def solution(n, costs):

    answer = [float('inf')]*n
    node = {x:[] for x in range(n)}

    for i in costs:
        node[i[0]] += [(i[2],i[1])]
        node[i[1]] += [(i[2],i[0])]

    heap = [(0,0)]

    while heap:
        cost, idx = heapq.heappop(heap)
        if cost < answer[idx]:
            answer[idx] = cost
            for i in node[idx]:
                heapq.heappush(heap,(i[0],i[1]))
        if idx == n-1:
            return sum(answer)
            
    return sum(answer)