def solution(dots):
    
    comb = [(0,1,2,3),(0,2,1,3),(0,3,1,2)]
    
    for i in comb:
        if dots[i[0]][0] - dots[i[1]][0] != 0 and dots[i[2]][0] - dots[i[3]][0] != 0:
            if (dots[i[0]][1] - dots[i[1]][1]) / (dots[i[0]][0] - dots[i[1]][0]) == (dots[i[2]][1] - dots[i[3]][1]) / (dots[i[2]][0] - dots[i[3]][0]):
                return 1
    return 0