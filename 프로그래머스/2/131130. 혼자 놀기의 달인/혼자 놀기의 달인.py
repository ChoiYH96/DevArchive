def solution(cards):
    answer = [0]

    for i in range(len(cards)):
        if cards[i] != 0:
            temp = []
            idx = i
            while cards[idx] != 0:
                temp += [cards[idx]]
                cards[idx] = 0
                idx = temp[-1]-1
            answer+=[len(temp)]
            
    answer.sort()
    
    return answer[-1]*answer[-2]