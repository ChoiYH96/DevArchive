def solution(s, skip, index):
    alpha = [chr(x) for x in range(ord('a'),ord('z')+1) if chr(x) not in skip]
    return "".join([alpha[(alpha.index(x)+index)%len(alpha)] for x in s])