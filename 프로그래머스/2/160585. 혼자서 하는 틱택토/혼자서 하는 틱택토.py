def solution(board):
    board = [[1 if x == "O" else -1 if x == "X" else 0 for x in y] for y in board]
    cnt = sum(sum(board, []))
    row = [sum(x) for x in board]
    col = [board[0][x]+board[1][x]+board[2][x] for x in range(0,3)]
    cross = [board[0][0]+board[1][1] + board[2][2],board[0][-1]+board[1][-2] + board[2][-3]]
    
    if cnt == 0 and 3 not in row+col+cross:
        return 1
    if cnt == 1 and -3 not in row+col+cross and row.count(3) < 2 and col.count(3) < 2:
        return 1
    return 0