def route(start, end, maps):
    temp = [start]
    news = [[-1,0],[1,0],[0,-1],[0,1]]
    maps = [[0 if maps[x][y] == "X" or [x,y] == start else 1 for y in range(len(maps[0]))] for x in range(len(maps))]
    visited = [x[:] for x in maps]
    
    while True:
        if len(temp) == 0:
            return -1
        for i in temp[:]:
            for j in news:
                idx = [i[0]+j[0],i[1]+j[1]]
                if 0<=idx[0]<len(maps) and 0<=idx[1]<len(maps[0]):
                    if idx == end:
                        return maps[i[0]][i[1]]+1
                    elif visited[idx[0]][idx[1]] != 0 and maps[idx[0]][idx[1]] == 1:
                        maps[idx[0]][idx[1]] = maps[i[0]][i[1]]+1
                        temp = temp + [idx]
                        visited[idx[0]][idx[1]] = 0
            temp = temp[1:]

def solution(maps):
    idx = dict()
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] in ["S","E","L"]:
                idx[maps[i][j]] = [i,j]
        if len(idx) == 3:
            break
    
    answer = [route(idx["S"],idx["L"],maps),route(idx["L"],idx["E"],maps)]
    
    return -1 if -1 in answer else sum(answer) 