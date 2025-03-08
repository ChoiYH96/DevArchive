def solution(maps):
    
    visited = [x[:] for x in maps]
    len_r,len_c = len(maps), len(maps[0])
    temp = [[0,0]]
    news = [[1,0],[-1,0],[0,1],[0,-1]]

    while True:
        if len(temp) == 0:
            return -1
        for i in temp[:]:
            for j in news:
                idx = [i[0]+j[0],i[1]+j[1]]
                if 0 <= idx[0] < len_r and 0 <= idx[1] < len_c:
                    if idx == [len_r-1,len_c-1]:
                        return maps[i[0]][i[1]] + 1
                    elif visited[idx[0]][idx[1]] != 0 and maps[idx[0]][idx[1]] == 1:
                        maps[idx[0]][idx[1]] = maps[i[0]][i[1]] + 1
                        visited[idx[0]][idx[1]] = 0
                        temp = temp+[idx]
            temp = temp[1:]