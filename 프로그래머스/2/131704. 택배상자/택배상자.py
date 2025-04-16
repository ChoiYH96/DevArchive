def solution(order):

    stack = []
    order.reverse()
    answer = 0

    for i in range(1,len(order)+1):
        if order[-1] == i:
            order.pop()
            answer+=1
            while stack:
                if stack[-1] == order[-1]:
                    order.pop()
                    stack.pop()
                    answer+=1
                else:
                    break
        else:
            stack+=[i]

    return answer