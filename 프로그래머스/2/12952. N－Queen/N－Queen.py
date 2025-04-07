def n_queen(n, lv, board):
    
    answer = 0
    
    if True not in board[lv]:
        return 0
    elif lv == 0:
        return 1
    else:
        for idx, val in enumerate(board[lv]):
            if val:
                temp = [board[x][:] for x in range(lv+1)]
                for row in range(lv+1):
                    temp[row][idx] = False
                    if idx+row < n:
                        temp[lv-row][idx+row] = False
                    if -1 < idx-row:
                        temp[lv-row][idx-row] = False
                answer += n_queen(n,lv-1,temp[:lv])
        return answer

def solution(n):
    arr = [[True]*n for _ in range(n)]
    return n_queen(n,n-1, arr)
                
    