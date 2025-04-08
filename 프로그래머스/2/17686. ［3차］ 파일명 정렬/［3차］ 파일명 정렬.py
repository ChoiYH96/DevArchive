def solution(files):

    files = [[y if not y.isdigit() else int(y) for y in files[x]] for x in range(len(files))]
    new_files = [[] for _ in  range(len(files))]
    
    for i in range(len(files)):
        temp = files[i][0]
        for j in range(1,len(files[i])):
            if type(files[i][j-1]) == type(files[i][j]):
                temp += str(files[i][j])
            else:
                new_files[i]+=[temp]
                temp = str(files[i][j])
        if temp != new_files[i][-1]:
            new_files[i]+=[temp]
    
    new_files = sorted(new_files, key = lambda x: (x[0].lower(),int(x[1])))
    
    return ["".join(x) for x in new_files]