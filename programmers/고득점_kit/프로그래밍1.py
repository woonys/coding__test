def solution(rounds):
    answer = 0
    base = ['a', 'b', 'c', 'd']
    prev_case = []
    exclude_case = []
    for round in rounds:
        if prev_case != []:
            for i in range(4):
                if (base[i], round[i]) in prev_case:
                    answer += 1
                    exclude_case.append((base[i], round[i]))
            prev_case = []
    
        for i in range(4):
            if base[i] == round[i]:
                answer += 1
            elif (base[i], round[i]) == (round[base.index(round[i])], base[base.index(round[i])]) and (base[i], round[i]) not in exclude_case:
                prev_case.append((base[i], round[i]))
    return answer

print(solution([["b", "a", "d", "c"],["b", "a", "c", "d"]]))