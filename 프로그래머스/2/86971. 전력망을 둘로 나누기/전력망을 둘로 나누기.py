def fn(t,arr):
    temp = 0
    for i in range(len(arr)):
        if t in arr[i]:
            temp += 1 + fn(arr[i][abs(arr[i].index(t)-1)],arr[:i]+arr[i+1:])
    return temp

def solution(n, wires):
    
    answer = 101
    
    for i in range(len(wires)):
        answer = min(answer,abs(fn(wires[i][1],wires[:i]+wires[i+1:])-fn(wires[i][0],wires[:i]+wires[i+1:])))
    
    return answer