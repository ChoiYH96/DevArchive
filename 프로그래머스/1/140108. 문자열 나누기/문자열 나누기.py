def solution(s):

    temp = ""
    answer = []
    
    for i in s:
        temp+=i
        if len(temp) == 2*temp.count(temp[0]):
            answer.append(temp)
            temp=""

    if temp != "":
        answer.append(temp)
        
    return len(answer)