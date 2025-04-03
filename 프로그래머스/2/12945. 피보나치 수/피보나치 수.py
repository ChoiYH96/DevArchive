def solution(n):
    
    n_1,n_2 = 1,0
    
    for i in range(2,n+1):
        n_1, n_2 = n_1+n_2, n_1
        
    return n_1%1234567
    