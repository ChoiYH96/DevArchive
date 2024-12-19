def solution(arr):
    
    arr.sort()
    cnt = 1   
    
    while True:
        for i in arr[:-1]:
            if cnt*arr[-1] % i != 0:
                break
            else:
                if i == arr[-2]:
                    return cnt*arr[-1]
                
        cnt+=1