def find_target(n, word, target, words):

    if word == target:
        return n
    else:
        answer = 51
        for i in range(len(words)):
            cnt = 0
            for j in range(len(word)):
                if word[j] != words[i][j]:
                    cnt+=1
            if cnt==1:
                temp = find_target(n+1, words[i], target, words[:i]+words[i+1:])
                if temp != 0:
                    answer = min(answer,temp)
        return answer if answer != 51 else 0
    
def solution(begin, target, words):
    if target not in words:
        return 0
    else:
        return find_target(0,begin, target, words)