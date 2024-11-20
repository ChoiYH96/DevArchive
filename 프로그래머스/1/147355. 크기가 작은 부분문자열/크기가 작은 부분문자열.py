def solution(t, p):
    return len([x for x in [int(t[y:y+len(p)]) for y in range(0,len(t)-len(p)+1)] if x <= int(p)])