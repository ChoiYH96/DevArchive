def sep_str(p):
    temp = ""
    
    if len(p) == 0:
        return ""
    elif p[0] == "(":
        cnt = 1
    else:
        cnt = -1

    if p[0] == "(":
        for i in range(1,len(p)):
            if p[i] == "(":
                cnt+=1
            else:
                cnt-=1
            if cnt == 0:
                return p[:i+1]+sep_str(p[i+1:])
    else:
        for i in range(1,len(p)):
            if p[i] == "(":
                cnt+=1
            else:
                cnt-=1
            if cnt == 0:
                temp += "(" + sep_str(p[i+1:])
                return temp+")"+"".join(["(" if x== ")" else ")" for x in p[:i+1][1:-1]])
                
                
def solution(p):
    answer = ''
    cnt = 0
    
    for i in p:
        if i == "(":
            cnt+=1
        else:
            cnt -= 1
        if cnt < 0: 
            break

    if cnt == 0:
        return sep_str(p)
    else:
        return sep_str(p)