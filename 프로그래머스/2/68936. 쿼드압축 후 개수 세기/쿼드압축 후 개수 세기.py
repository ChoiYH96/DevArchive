def solution(arr):

    temp = 0
    
    for i in arr:
        temp+=sum(i)
        
    if temp == 0:
        return [1,0]
    elif temp == len(arr)**2:
        return [0,1]
    
    area = len(arr)//2
    
    answer = [0,0]
    while area >= 2:
        for i in range(0,len(arr),area):
            for j in range(0,len(arr),area):
                temp=0
                if arr[i][j] != -1:
                    for k in range(area):
                        temp+=sum(arr[i+k][j:j+area])
                        
                    if temp == 0:
                        answer[0]+=1
                        for l in range(area):
                            arr[i+l][j:j+area]=[-1]*area

                    elif temp == area*area:
                        answer[1]+=1
                        for l in range(area):
                            arr[i+l][j:j+area]=[-1]*area

        area=area//2
        
    for i in arr:
        answer[0] += i.count(0)
        answer[1] += i.count(1)
        
    return answer