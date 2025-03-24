def solution(n, s):
    
    answer = []
    
    for i in range(n,0,-1):
        temp = s//i
        s -= temp
        if temp == 0: return [-1]
        answer += [temp]
        
    return answer