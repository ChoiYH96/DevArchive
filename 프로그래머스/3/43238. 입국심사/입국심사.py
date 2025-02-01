def solution(n, times):
    
    start, end = 0, n*max(times)
    answer = n*max(times)

    while start < end:
        temp = (start+end)//2
        cnt = 0
        for i in times:
            cnt += temp//i
        if cnt < n:
            start = temp + 1
        else:
            end = temp 
            answer = min(answer,temp)
            
    return answer