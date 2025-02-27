def solution(m, n, board):
    
    board = [[board[y][x] for y in range(m)] for x in range(n)]
    answer = 0

    while True:
        temp = []
        for i in range(len(board)-1):
            for j in range(len(board[0])-1):
                if board[i][j] != 0 and len(set(board[i][j:j+2] + board[i+1][j:j+2])) == 1:
                    temp+=[(i,j),(i,j+1),(i+1,j),(i+1,j+1)]

        if len(temp) == 0:
            return answer
        
        temp = sorted(set(temp), key = lambda x: (x[0],x[1]))
        
        for i in temp:
            board[i[0]][i[1]] = 0
            answer+=1
        
        for i in range(len(board)):
            board[i] = [0]*board[i].count(0)+[x for x in board[i] if x != 0]