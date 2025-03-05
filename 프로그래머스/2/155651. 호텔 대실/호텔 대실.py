def solution(book_time):
    
    book_time = sorted(book_time, key = lambda x: x[0])
    answer = [[book_time[0]]]

    for i in book_time[1:]:
        for j in range(len(answer)):
            temp = str(int(answer[j][-1][1][:2])+(int(answer[j][-1][1][3:])+10)//60).zfill(2) +":"+str((int(answer[j][-1][1][3:])+10)%60).zfill(2)
            if temp <= i[0]:
                answer[j]+=[i]
                break
            elif j == len(answer)-1:
                answer+=[[i]]
                break

    return len(answer)