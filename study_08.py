def solution(skill, skill_trees):
    answer = 0
    for i in range(len(skill_trees)):
        tmp = []
        for j in range(len(skill)):
            if skill_trees[i].find(skill[j]) >= 0: 
                tmp.append(skill_trees[i].find(skill[j]))
        print(tmp)
        print(sorted(tmp))
        if tmp == sorted(tmp) and skill[0] in skill_trees[i]:
            answer += 1
    print(answer)
    return answer
solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])