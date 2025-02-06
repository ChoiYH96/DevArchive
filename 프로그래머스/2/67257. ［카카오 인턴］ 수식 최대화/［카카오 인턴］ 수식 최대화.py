import itertools as it

def calc(n1,n2,oper):
    if oper == "+":
        return n1 + n2
    if oper == "-":
        return n1 - n2
    if oper == "*":
        return n1 * n2
    else:
        return n1 / n2
    
def solution(expression):
    
    cal_prio = ["".join(x) for x in it.permutations(set([x for x in expression if x != "!" and not x.isdigit()]))]
    temp =""
    exp_list = []
    answer = []
    
    for i in expression+"!":
        if i.isdigit():
            temp+=i
        elif i != "!":
            exp_list+=[int(temp),i]
            temp = ""
        else:
            exp_list.append(int(temp))

    for i in cal_prio:
        temp = exp_list[:]
        for j in i:
            while (j in temp):
                for k in range(len(temp)):
                    if temp[k] == j:
                        temp = temp[:k-1] + [calc(temp[k-1],temp[k+1],temp[k])] + temp[k+2:]
                        break
        answer.append(int(temp[0]))
        
    return max([abs(x) for x in answer])