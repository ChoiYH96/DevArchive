n, s = map(int, input().split())
arr = list(map(int, input().split()))
prefix = [0]
answer = n+1

for i in arr:
    prefix += [prefix[-1] + i]

start, end = 0, 0
while end != len(prefix):
    if prefix[end] - prefix[start] >= s:
        answer = min(answer, end - start)
        start += 1
    elif prefix[end] - prefix[start] < s:
        end += 1

print(answer if answer != len(arr)+1 else 0)