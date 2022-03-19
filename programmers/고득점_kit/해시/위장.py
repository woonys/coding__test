'''
How to solve? 답안 참고
왜 못 풀었나? 내가 접근한 방식을 보자.

각 wear: w
하나의 wear 종류에 해당하는 옷의 개수: a라고 하자.
그러면
w1: a1
w2: a2
.
.
.
wn: an
이런 식으로 짝이 지어질 것.

이렇게 되면 나오는 값은
a1+ a2 + a3 + ... + an
a1a2 + a2a3 + .. + an-1an
.
.
a1a2a3...an
이를 모두 더한 값이 될 것.

여기서 문제: 이걸 코드로 어떻게 옮겨야 하지...?
처음 생각: dfs -> 떠오르지 않음..
여기서 막혀서 뭔가 접근을 잘못했다 느끼고 답안 참고.
그냥 안 입는 경우의 수를 각 케이스에 더해주고
마지막에 아무 것도 안 입는 케이스 한 가지만 빼주면 끝.

사실상 수학 문제.

시간 복잡도: O(N) -> for문 병렬로 두 번 돈다.
공간 복잡도: O(N) -> dic에 주어진 wear 종류 갯수만큼 채워짐 
'''
from collections import defaultdict
def solution(clothes):
    dic = defaultdict(int)
    for cloth in clothes:
        dic[cloth[1]] += 1

    answer = 1
    for key, value in dic.items():
        answer *= (value+1)

    return answer-1