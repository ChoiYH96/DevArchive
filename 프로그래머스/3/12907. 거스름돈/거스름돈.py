def solution(n, money):
    
    charge = [1]+[0]*n
    
    for i in money:
        for j in range(i,n+1):
            charge[j] += charge[j-i]

    return charge[-1]