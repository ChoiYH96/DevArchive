def solution(n):
    answer = n
    while True:
        answer +=1
        if bin(answer).count("1") == bin(n).count("1"):
            return answer
        