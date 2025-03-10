from collections import deque

r, c = map(int, input().split())

maps = []
idx = dict()
cnt = 0
news = [[1,0],[-1,0],[0,1],[0,-1]]

for i in range(r):
    maps += [list(input())]

for i in range(r):
    for j in range(c):
        if maps[i][j] in ["S","D"]:
            idx[maps[i][j]] = [i,j]

temp = deque([idx["S"]])

while True:
    flood = []

    if len(temp) == 0:
        print("KAKTUS")
        break

    for i in range(r):
        for j in range(c):
            if maps[i][j] == "*":
                for k in news:
                    if 0 <= i+k[0] < r and 0 <= j+k[1] < c:
                        if maps[i+k[0]][j+k[1]] not in ["D","X"]:
                            flood+=[[i+k[0],j+k[1]]]
    for i in flood:
        maps[i[0]][i[1]] = "*"

    for i in temp.copy():
        maps[i[0]][i[1]] = cnt
        for j in news:
            if 0 <= i[0]+j[0] < r and 0 <= i[1]+j[1] < c:
                if [i[0]+j[0],i[1]+j[1]] == idx["D"]:
                    maps[i[0]][i[1]] = cnt
                    print(cnt+1)
                    exit()
                elif maps[i[0]+j[0]][i[1]+j[1]] == ".":
                    temp += [[i[0]+j[0],i[1]+j[1]]]
                    maps[i[0]+j[0]][i[1]+j[1]] = 1+cnt
        temp.popleft()
    cnt+=1
