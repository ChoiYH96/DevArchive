from collections import deque

def solution(queue1, queue2):

    q1, q2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(q1), sum(q2)
    cnt = len(q1)
    answer = 0

    while sum1 != sum2:
        if sum1 > sum2:
            q2.append(q1.popleft())
            sum1-=q2[-1]
            sum2+=q2[-1]
            answer+=1
        elif sum1 < sum2:
            q1.append(q2.popleft())
            sum2 -= q1[-1]
            sum1 += q1[-1]
            answer += 1
            cnt-=1
        if cnt == 0:
            return -1
        
    return answer