'''
Runtime: 38 ms, faster than 78.51% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 13.9 MB, less than 88.60% of Python3 online submissions for Longest Common Prefix.
시간복잡도: O(N*M)
    - N: 기준으로 잡은(stand = str[0]) 문자열의 길이(문자 수)
    - M: 리스트 strs의 원소 수
공간복잡도: O(N) -> 추가로 활용하는 공간은 ans-> 메모리에 차지하는 ans의 최대 길이는 stand 길이에 해당

how to solve?
1. 주어진 strs를 sorting -> 길이가 짧은 순으로 정렬: sort(key=len) 사용
    Question: 바로 아래 솔루션 보면, 실수로 key=len 조건을 빠뜨린 채 sort를 사용했는데도 문제가 풀렸다 (속도는 이 솔루션이 더 빠름)
    어떻게 풀린 거지...? key=len을 빼면 알파벳 순서로 정렬될텐디...? 예제 케이스 오류일지도..?
2. 길이가 가장 짧은 문자열을 기준(stand)로 설정 -> 만약 얘보다 긴 애를 기준으로 하면 아래 이중 for문 도는 과정에서 index 초과 발생
3. 이중 for문: 
    1) 먼저 stand의 길이를 기준으로 한 글자씩 for문을 돌고
    2) 그 다음 strs에 들어있는 각 문자열을 하나씩 꺼내서 stand의 문자열에서 꺼낸 애와 일치하는지 비교한다
    3) 중간에 틀리면 바로 ans를 return
    4) 모두 다 통과하면 가장 짧은 문자열인 stand가 정답이 될 것이니 해당 값을 return

'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        strs.sort(key=len)
        stand = strs[0]
        for word in range(len(stand)):
            for i in strs:
                if i[word] != stand[word]:
                    return ans
            ans += stand[word]
        return ans


'''
Runtime: 43 ms, faster than 63.62% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 14.1 MB, less than 11.80% of Python3 online submissions for Longest Common Prefix.

How to solve?
1. 먼저 sort해서 길이가 가장 짧은 글자 순으로 나열한다. -> 여기는 알파벳 순으로 정렬했는데 why 통과..? 미스테리..
시간복잡도: O(N^2) -> stand로 잡은 글
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        strs.sort()
        stand = strs[0] 
        for word in range(len(stand)):
            for i in strs:
                if i[word] != stand[word]:
                    return ans
            ans += stand[word]
        return ans