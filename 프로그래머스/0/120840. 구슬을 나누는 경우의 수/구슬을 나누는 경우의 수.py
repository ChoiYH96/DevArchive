def factorial(x):
    answer = 1
    for i in range(1,x+1):
        answer*=i
    return answer

def solution(balls, share):
    return factorial(balls)/(factorial(balls-share)*factorial(share))