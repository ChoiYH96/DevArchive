def solution(p):
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
                return p[:i+1]+solution(p[i+1:])
    
    else:
        for i in range(1,len(p)):
            if p[i] == "(":
                cnt+=1
            else:
                cnt-=1
            if cnt == 0:
                temp += "(" + solution(p[i+1:])
                return temp+")"+"".join(["(" if x== ")" else ")" for x in p[:i+1][1:-1]]) 