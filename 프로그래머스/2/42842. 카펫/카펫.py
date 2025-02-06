def solution(brown, yellow):
    
    n = brown+ yellow
    
    for i in range(2,n):
        if n%i == 0:
            if (n//i-2) * (i-2) == yellow:
                return [n//i, i]