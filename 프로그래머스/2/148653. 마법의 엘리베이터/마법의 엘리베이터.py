def solution(storey):
    answer = 0
    while storey > 0:
        if storey % 10 > 5 or (storey%10 == 5 and storey//10%10) >= 5 :
            temp = 10 - storey % 10
            answer += temp
            storey += temp
            storey //= 10
        else:
            answer += storey % 10
            storey //= 10  
    return answer