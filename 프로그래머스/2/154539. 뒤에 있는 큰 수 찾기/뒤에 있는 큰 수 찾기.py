def solution(numbers):
    
    answer = [-1]*len(numbers)
    temp = []
    for i in range(len(numbers)):
        for j in range(len(temp)-1,-1,-1):
            if numbers[i] > numbers[temp[j]]:
                answer[temp[j]] = numbers[i]
                temp.pop(j)
            else:
                break
        temp+=[i]
    
    return answer