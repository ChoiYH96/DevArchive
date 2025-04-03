def solution(n):
    
    n1,n2 = 1,1
    
    for i in range(2,n+1):
        n1, n2 = n1+n2, n1
        
    return n1%1000000007