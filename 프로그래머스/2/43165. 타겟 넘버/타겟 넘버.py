def target_number(numbers,target,n):
    if n == len(numbers) and sum(numbers) == target:
        return 1
    elif n == len(numbers):
        return 0
    else:
        return target_number(numbers,target,n+1) +  target_number(numbers[:n]+[-numbers[n]]+numbers[n+1:],target,n+1)


def solution(numbers, target):
    return target_number(numbers,target,0)