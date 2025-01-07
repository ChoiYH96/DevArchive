def solution(n, results):
    # 승패 관계를 담을 2D 배열 초기화
    wins = [[0] * n for _ in range(n)]
    
    # 경기 결과에 따라 wins 배열을 초기화
    for a, b in results:
        wins[a-1][b-1] = 1  # a가 b를 이김
        wins[b-1][a-1] = -1 # b가 a에게 짐
    
    # 플로이드 와샬 알고리즘 적용 (모든 쌍 최단 경로, 여기서는 승패 관계)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if wins[i][k] == 1 and wins[k][j] == 1:  # i -> k, k -> j
                    wins[i][j] = 1  # i가 j를 이김
                if wins[i][k] == -1 and wins[k][j] == -1:  # i -> k, k -> j
                    wins[i][j] = -1  # i가 j에게 짐
    
    # 정확한 순위를 매길 수 있는 선수 수 계산
    answer = 0
    for i in range(n):
        count = 0
        for j in range(n):
            if wins[i][j] != 0:  # i와 j의 승패 관계가 확실
                count += 1
        if count == n - 1:  # 다른 모든 선수와 승패 관계가 확실하면
            answer += 1
    
    return answer