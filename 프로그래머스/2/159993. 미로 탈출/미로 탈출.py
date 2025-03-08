def route_start_lever(maps):
    cnt = 1
    temp = []
    news = [[-1,0],[1,0],[0,-1],[0,1]]
    maps = [[0 if y == "X" else y if y in ["S","L"] else 1 for y in x] for x in maps]
    visited = [x[:] for x in maps]
        
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "S":
                temp = [[i,j]]
        if len(temp) != 0:
            break

    while True:
        if len(temp) == 0:
            break
        for i in temp[:]:
            for j in news:
                idx = [i[0]+j[0],i[1]+j[1]]
                if 0<=idx[0]<len(maps) and 0<=idx[1]<len(maps[0]):
                    if maps[idx[0]][idx[1]] == "L":
                        return cnt
                    elif visited[idx[0]][idx[1]] != 0 and maps[idx[0]][idx[1]] == 1:
                        maps[idx[0]][idx[1]] = cnt
                        temp = temp + [idx]
                        visited[idx[0]][idx[1]] = 0
            temp = temp[1:]
        cnt+=1
        
    return -1

def route_lever_exit(maps):
    cnt = 1
    temp = []
    news = [[-1,0],[1,0],[0,-1],[0,1]]
    maps = [[0 if y == "X" else y if y in ["E","L"] else 1 for y in x] for x in maps]
    visited = [x[:] for x in maps]
        
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "L":
                temp = [[i,j]]
        if len(temp) != 0:
            break

    while True:
        if len(temp) == 0:
            break
        for i in temp[:]:
            for j in news:
                idx = [i[0]+j[0],i[1]+j[1]]
                if 0<=idx[0]<len(maps) and 0<=idx[1]<len(maps[0]):
                    if maps[idx[0]][idx[1]] == "E":
                        return cnt
                    elif visited[idx[0]][idx[1]] != 0 and maps[idx[0]][idx[1]] == 1:
                        maps[idx[0]][idx[1]] = cnt
                        temp = temp + [idx]
                        visited[idx[0]][idx[1]] = 0
            temp = temp[1:]
        cnt+=1
        
    return -1

def solution(maps):
    answer = [route_start_lever(maps), route_lever_exit(maps)]
    return sum(answer) if -1 not in answer else -1
            
    
    