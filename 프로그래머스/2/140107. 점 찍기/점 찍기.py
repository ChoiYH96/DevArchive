def solution(k, d):
    answer = 0
    max_idx = int(d/(2**(1/2)))

    for i in range(0,max_idx+1,k):
        answer+= (int(((d-i)*(d+i))**(1/2))-i)//k

    return answer*2+max_idx//k+1