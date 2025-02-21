def solution(babbling):
    pron = {"aya" : "1", "ye" : "2", "woo" : "3", "ma" : "4"}
    for i in pron.keys():
        for j in range(len(babbling)):
            babbling[j] = babbling[j].replace(i,pron[i])
    
    for i in ["11","22","33","44"]:
        for j in range(len(babbling)):
            babbling[j] = babbling[j].replace(i,"repeat")
                
    return len([x for x in babbling if x.isdigit()])