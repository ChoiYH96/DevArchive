def solution(N, stages):
    f_rate = []
    user = len(stages)
    
    for i in range(1,N+1):
        f_user = stages.count(i)
        if f_user != 0:
            f_rate += [[i,f_user/user]]
            user -= f_user
        else:
            f_rate += [[i, 0.0]]
    
    f_rate.sort(key = lambda x : (-x[1], x[0]))
    
    return [x[0] for x in f_rate]