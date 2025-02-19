def solution(a, b):
    
    for i in range(2,a+1):
        if a % i == 0 and b % i == 0:
            a = int(a/i)
            b = int(b/i)
            
    while b > 1:
        if b % 2 == 0:
            b = int(b/2)
        elif b % 5 == 0:
            b = int(b/5)
        else:
            return 2
    return 1