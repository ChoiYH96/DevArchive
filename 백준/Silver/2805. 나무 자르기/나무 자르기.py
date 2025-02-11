n, m = map(int, input().split())

trees = list(map(int, input().split()))
min_h, max_h = 1, 1000000000

while min_h <= max_h:
    mid = (min_h + max_h)//2
    temp = 0
    for i in trees:
        if i - mid > 0:
            temp += i-mid

    if temp < m:
        max_h = mid - 1
    else:
        min_h = mid + 1
print(max_h)