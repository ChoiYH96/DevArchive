def solution(citations):
    citations.sort()

    for i in range(min(citations[-1],len(citations)),-1,-1):
        for j in range(len(citations)):
            if citations[j] >= i and j <= i and len(citations) - j >= i:
                return i