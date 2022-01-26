'''
How to solve: my solution
Runtime: 175 ms, faster than 31.46% of Python3 online submissions for UTF-8 Validation.
Memory Usage: 14.7 MB, less than 19.01% of Python3 online submissions for UTF-8 Validation.

시간복잡도: O(N): while문으로 pop하면서 진행
공간복잡도: O(1): 데크로 상수 크기 공간 복사
'''

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        
        range_0 = 0
        range_10 = 1<<1
        range_110 = 1<<2|1<<1
        range_1110 = 1<<3|1<<2|1<<1
        range_11110 = 1<<4|1<<3|1<<2|1<<1
        
        
        dq = collections.deque(data)
        
        while dq:
            i = dq.popleft()
            if range_11110 == (i>>3):
                if len(dq) < 3:
                    return False
                for x in range(3):
                    num = dq.popleft()
                    if (num>>6) != range_10:
                        return False
                continue
            elif range_1110 == (i>>4):
                if len(dq) < 2:
                    return False
                for x in range(2):
                    num = dq.popleft()
                    if (num>>6) != range_10:
                        return False
                continue
            # case 1: 11110xxx
            elif range_110 == (i>>5):
                if len(dq) < 1:
                    return False
                num = dq.popleft()
                if (num>>6) != range_10:
                        return False
                continue
            elif range_0 == (i>>7):
                continue
                
            else:
                return False
            
        
        return True
        
        