def solution(dirs):
    
    udrl = {"U" : [0,1],"D": [0,-1], "R": [1,0], "L": [-1,0]}
    start = [0,0]
    answer = []
    
    for i in dirs:
        move = [start[0]+udrl[i][0],start[1]+udrl[i][1]]
        if -5 <= move[0] <= 5 and -5 <= move[1] <= 5:
            answer += [sorted([tuple(start),tuple(move)])]
            start = move
    
    return len(set(tuple(x) for x in answer))