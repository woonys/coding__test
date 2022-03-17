from collections import defaultdict
def solution(clothes):
    dic = defaultdict(int)
    for cloth in clothes:
        dic[cloth[1]] += 1
    print(dic.values)
        
print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))