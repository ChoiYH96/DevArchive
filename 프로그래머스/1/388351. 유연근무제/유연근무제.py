def solution(schedules, timelogs, startday):
    
    schedules = [(x//100+(((x%100)+10)//60))*100+((x%100)+10)%60 for x in schedules]
    newlogs = [[timelogs[x][(1-startday)+y] for y in range(0,5)] for x in range(len(timelogs))]    
    
    return len([x for x in [[newlogs[y][z] for z in range(0,5) if schedules[y] >= newlogs[y][z]] for y in range(len(newlogs))] if len(x) == 5])