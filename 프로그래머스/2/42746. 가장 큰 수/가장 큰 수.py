def solution(a): 
    
    
    a = sorted(list(map(str, a)), key = lambda x: x*3, reverse=True)
    
    return "".join(a) if a[0] != "0" else "0"