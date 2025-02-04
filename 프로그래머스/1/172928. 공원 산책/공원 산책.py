def solution(park, routes):
    answer = [[x,y] for x in range(len(park)) for y in range(len(park[0])) if park[x][y] == "S"][0]
    col, row = len(park[0]), len(park)
    
    for i in routes:
        direction, cnt = i.split()
        cnt = int(cnt)
        if direction =="N" and answer[0] - cnt >= 0:
            if len([x for x in range(cnt+1) if park[answer[0]-x][answer[1]] == "X"]) == 0:
                answer[0]-=cnt
                print(i, answer)
        elif direction == "S" and answer[0] + cnt < row:
            if len([x for x in range(cnt+1) if park[answer[0]+x][answer[1]] == "X"]) == 0:
                answer[0]+=cnt
                print(i, answer)
        elif direction == "W" and answer[1] - cnt >= 0:
            if len([x for x in range(cnt+1) if park[answer[0]][answer[1]-x] == "X"]) == 0:
                answer[1]-=cnt
                print(i, answer)
        elif direction == "E" and answer[1] + cnt < col:
            if len([x for x in range(cnt+1) if park[answer[0]][answer[1]+x] == "X"]) == 0:
                answer[1]+=cnt
                print(i, answer)
        
    return answer