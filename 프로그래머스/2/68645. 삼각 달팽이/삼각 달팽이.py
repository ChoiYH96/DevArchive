def solution(n):
    snail = [[0] * x for x in range(1,n+1)]
    temp = 0
    row, col = 0, 0
    
    for i in range(n,0,-1):
        if (n-i)%3 == 0:
            for j in range(i):
                temp+=1
                snail[row+j][col] = temp
            row += j
            col += 1
        elif (n-i)%3 == 1:
            for j in range(i):
                temp+=1
                snail[row][col+j] = temp
            col = (col+j-1)
            row -= 1
        else:
            for j in range(i):
                temp+=1
                snail[row-j][col-j] = temp
            row = (row-j+1)
            col -= j
            
    return [snail[x][y] for x in range(len(snail)) for y in range(len(snail[x]))]