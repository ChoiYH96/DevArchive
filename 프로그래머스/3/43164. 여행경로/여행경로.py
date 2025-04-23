def find_route(temp, route, tickets,cnt):
    if not tickets:
        return route+[temp]
    elif temp not in [x[0] for x in tickets]:
        return []
    else:
        answer = []
        for idx,country in enumerate(tickets):
            if country[0] == temp:
                answer = find_route(country[1], route+[country[0]],tickets[:idx]+tickets[idx+1:],cnt)
            if len(answer) == cnt:
                return answer
        return answer

def solution(tickets):
    tickets = sorted(tickets, key = lambda x: (x[0],x[1]))
    answer = find_route("ICN",[],tickets, len(tickets)+1)
    return answer