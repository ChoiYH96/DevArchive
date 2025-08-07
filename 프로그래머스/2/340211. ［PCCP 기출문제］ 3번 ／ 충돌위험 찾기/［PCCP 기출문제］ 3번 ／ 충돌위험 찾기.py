def solution(points, routes):
    
    time_stamp = []
    
    for route in routes:
        temp = [points[route[0]-1]]
        for path in route[1:]:
            dx, dy = 1 if temp[-1][0] < points[path-1][0] else -1,1 if temp[-1][1] < points[path-1][1] else -1
            for _ in range(abs(temp[-1][0] - points[path-1][0])):
                temp.append([temp[-1][0] + dx, temp[-1][1]])
            for _ in range(abs(temp[-1][1] - points[path-1][1])):
                temp.append([temp[-1][0],temp[-1][1] + dy])
        time_stamp.append(temp)
    
    answer = set()

    for i in range(len(time_stamp)-1):
        for j in range(i+1,len(time_stamp)):
            for k in range(min(len(time_stamp[i]), len(time_stamp[j]))):
                if time_stamp[i][k] == time_stamp[j][k]:
                    answer.add(tuple([k]+time_stamp[i][k]))
                    
    return len(answer)