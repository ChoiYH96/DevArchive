def solution(s):
    answer = sorted([set(map(int, x.split(","))) for x in s[2:len(s)-2].split("},{")], key = lambda x: len(x))
    return list(answer[0]) if len(answer) == 1 else list(answer[0])+[list(answer[x]-answer[x-1])[0] for x in range(1,len(answer))]