def solution(n, m, section):
    
    if not section: return 0
    
    answer = 1
    temp = section[0]
    
    for i in section[1:]:
        if i-temp > m-1:
            answer+=1
            temp = i
            
    return answer