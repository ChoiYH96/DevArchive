def max_value(arr):
    min_value,max_value = 0,max(arr)
    prefix = [0]
    
    for i in range(len(arr)):
        prefix+=[prefix[-1]+arr[i]]

    for i in range(1,len(prefix)):
        max_value = max(max_value,prefix[i]-min_value)
        min_value = min(min_value, prefix[i])
        
    return max_value

def solution(sequence):
    pulse1 = [sequence[x]*((-1)**x) for x in range(len(sequence))]
    pulse2 = [sequence[x]*((-1)**(x+1)) for x in range(len(sequence))]
    
    return max(max_value(pulse1),max_value(pulse2))