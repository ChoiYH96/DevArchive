def solution(skill, skill_trees):
    
    possible_trees = [list(skill[:x]) for x in range(1,len(skill)+1)]
    skill_trees = [[y for y in x if y in skill] for x in skill_trees]
    
    return len([x for x in skill_trees if x in possible_trees or len(x) == 0])