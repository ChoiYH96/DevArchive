from collections import deque

def solution(topping):
    answer = 0 
    cnt = {x:0 for x in set(topping)}
    divide = set()
    
    for i in topping:
        cnt[i]+=1
    
    for i in topping:
        divide.add(i)
        cnt[i] -= 1
        if cnt[i] == 0:
            del cnt[i]
        if len(cnt) == len(divide):
            answer+=1
    
    return answer