def cnt_divisor(n):
    cnt = 0
    for i in range(1,int(n**(1/2))+1):
        if n%i == 0:
            if i != n**(1/2):
                cnt += 2
            else:
                cnt += 1
    return cnt
    
def solution(number, limit, power):    
    return sum([x if x <= limit else power for x in [cnt_divisor(y) for y in range(1,number+1)]])