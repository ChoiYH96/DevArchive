def solution(n, t, m, p):
    
    answer = "0"
    num = 0
    alpha = ['A','B','C','D','E','F']
    
    while len(answer) <= t*m:
        
        num+=1
        temp = num
        cvt = ""
        
        while temp > 0:
            temp, mod = divmod(temp, n)
            if mod < 10:
                cvt += str(mod)
            else:
                cvt += alpha[mod%10]             
        answer+=cvt[::-1]
        
    return "".join([answer[(p-1)+m*x] for x in range(t)])