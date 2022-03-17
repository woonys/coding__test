# 전화번호 목록: https://programmers.co.kr/learn/courses/30/lessons/42577

# How to solve: 답안 참고..
# 왜 혼자 못 풀었지?: 해시를 써서 키값과 특정 값을 비교할 때, 어디까지 잘라서 비교해야 할지가 막막했음 => temp와 for문으로 해결
# 시간복잡도: O(N**2) => 최대 100만개 phone_num과 각 phone_num 길이 최대 20 => 2000만.
# 공간복잡도: O(N) => hash_map에 들어가는 key: 모든 phone_num이 들어감.


def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_num in phone_book:
        hash_map[phone_num] = 1
    
    for phone_num in phone_book:
        temp = ""
        for num in phone_num:
            temp += num
            if temp in hash_map and temp != phone_num: # 자기 자신이 무조건 hash_map에 존재할 수밖에 없음.
                return False
    return answer

print(solution(["123","456","789"]))