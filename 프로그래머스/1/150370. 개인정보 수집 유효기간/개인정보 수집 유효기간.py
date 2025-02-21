def solution(today, terms, privacies):

    terms = {x.split()[0] : int(x.split()[1]) for x in terms}
    
    for i in range(len(privacies)):
        year, month = int(privacies[i][0:4]), int(privacies[i][5:7])
        for j in range(terms[privacies[i][-1]]):
            if month == 12:
                month = 1
                year +=1
            else:
                month+=1
        privacies[i] = str(year)+"."+str(month).zfill(2)+privacies[i][7:10]

    return [x+1 for x in range(len(privacies)) if privacies[x] <= today]
    