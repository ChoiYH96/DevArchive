def solution(m, n, puddles):
    maps = [[0]*(m+1) for _ in range(n+1)]
    maps[1][0] = 1
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if [j,i] not in puddles:
                maps[i][j] = (maps[i-1][j] + maps[i][j-1])
    
    return maps[n][m]%1000000007