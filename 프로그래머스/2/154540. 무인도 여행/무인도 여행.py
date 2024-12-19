import sys 
sys.setrecursionlimit(10000)

def find_sector(row, col, arr):
    if row in (-1,len(arr)) or col in (-1,len(arr[0])):
        return 0
    else:
        if arr[row][col] == "X":
            return 0
        else:
            cnt = int(arr[row][col])
            arr[row][col] = "X"
            return cnt + find_sector(row-1, col, arr) + find_sector(row, col-1, arr) + find_sector(row+1, col, arr) + find_sector(row, col+1, arr)
        
def solution(maps):
    
    if "".join(maps).replace("X","") == "":
        return [-1]
    
    a = [list(x) for x in maps]

    answer = []

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if a[i][j] != "X":
                temp = find_sector(i, j, a)
                answer.append(temp)
                
    return sorted(answer)