import itertools as it

def solution(numbers):
    
    answer = 0
    
    per_num = set([int("".join(map(str, y))) for y in sum([list(it.permutations(numbers,x)) for x in range(1,len(numbers)+1)],[])])

    for i in per_num:
        if i > 2:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                answer+=1
        elif i == 2:
            answer+=1
        
    return answer