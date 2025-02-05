def solution(keymap, targets):
    
    answer = []
    
    key_list = set("".join(keymap))
    
    cnt = { x: 101 for x in key_list}
    
    for i in keymap:
        for idx,j in enumerate(i):
            cnt[j] = min(cnt[j],idx+1)
    
    for i in targets:
        temp = 0
        for j in i:
            if j not in key_list:
                temp = -1
                break
            else:
                temp+=cnt[j]
        answer+=[temp]
                 
    return answer