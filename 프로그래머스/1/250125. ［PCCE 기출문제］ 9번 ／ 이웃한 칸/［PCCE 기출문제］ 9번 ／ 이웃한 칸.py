def solution(board, h, w):
    return sum([1 if  -1 < h-x[0] < len(board) and -1 < w-x[1] < len(board[0]) and board[h][w] == board[h-x[0]][w-x[1]] else 0 for x in [(1,0),(-1,0),(0,1),(0,-1)]])