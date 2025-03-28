from collections import deque

def solution(A, B):
    A, B = deque(sorted(A)), deque(sorted(B))
    answer = 0
    
    for i in range(len(A)):
        if A[0] < B[0]:
            answer+=1
            A.popleft()
            B.popleft()
        else:
            A.pop()
            B.popleft()
        
    return answer