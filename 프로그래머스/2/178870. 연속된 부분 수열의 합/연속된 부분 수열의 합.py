def solution(sequence, k):
    
    if k in sequence: return [sequence.index(k)]*2
            
    r = [0,len(sequence)]
    temp = sequence[0]
    s,e = 0,0

    while True:
        if temp == k:
            r = [s,e] if e - s < r[1] - r[0] else [s,e] if e - s == r[1] - r[0] and s < r[0] else r
            e+=1
            if e >= len(sequence): return r
            else: temp+=sequence[e] 
        elif temp < k:
            e+=1
            if e >= len(sequence): return r
            else: temp+=sequence[e] 
        else:
            temp-=sequence[s]
            s+=1
    return r