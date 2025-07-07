def solution(mats, park):
    
    park = [ [0 if y != "-1" else 1 for y in park[x]] for x in range(len(park))]
    max_value = 1
    
    for i in range(1,len(park)):
        for j in range(1,len(park[0])):
            if park[i][j] == 1:
                park[i][j] += min(park[i-1][j],park[i][j-1],park[i-1][j-1])
                max_value = max(max_value, park[i][j])
    
    for i in sorted(mats, reverse = True):
        if i <= max_value:
            return i   
    
    return -1