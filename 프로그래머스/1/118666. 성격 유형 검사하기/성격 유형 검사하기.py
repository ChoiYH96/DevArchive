def solution(survey, choices):
    score = { x : 0 for x in ['R','T','C','F','J','M','A','N']}
    
    for i in range(len(survey)):
        if choices[i] < 4:
            score[survey[i][0]] += 4-choices[i]
        elif choices[i] > 4:
            score[survey[i][1]] += choices[i]-4
    
    return "".join([x[0] if score[x[0]] >= score[x[1]] else x[1] for x in ['RT','CF','JM','AN']])