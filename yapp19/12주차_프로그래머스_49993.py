def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        skill_list = list(skill)
        for now in skill_tree:
            if now in skill_list:
                if now != skill_list.pop(0): break
        else: answer += 1
                
    return answer
