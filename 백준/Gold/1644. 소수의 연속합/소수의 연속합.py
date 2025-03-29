n = int(input())

if n == 1:
    print(0)
    exit() 
    
prime = [x for x in range(2,n+1)]

for i in range(len(prime)):
    if prime[i] != 0:
        for j in range(i+prime[i],len(prime),prime[i]):
            prime[j] = 0

prime = [x for x in prime if x != 0]

answer = prime.count(n)

prefix = [0]

for i in range(0,len(prime)-1):
    prefix+=[prefix[-1]+prime[i]]

start, end = 0,0

while end != len(prefix):
    if prefix[end] - prefix[start] < n:
        end += 1
    elif prefix[end] - prefix[start] > n:
        start += 1
    else:
        answer+=1
        end += 1
        
print(answer)