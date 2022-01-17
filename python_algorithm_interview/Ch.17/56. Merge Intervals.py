'''
How to solve? : my sol
- 시간 복잡도: O(nlogn => 굳이 정렬 2번(아래 for문)해서 & 공간 복사로 낭비)
- 공간 복잡도: O(N)

최적화 작업: 아래 코드는 원본 => 
1. for문 제거하고(이미 sort로 정렬했으니까)
2. inter_cp 사용 X 하면

시간복잡도 최적화 가능! (10배 개선)
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # Solution 1
        # 총 세 가지 경우의 수: 
        #  1) 아예 안 겹치거나 => 패스
        #  2) 앞 인터벌 뒷자리와 뒤 인터벌 앞자리가 겹치거나 => 앞 인터벌 앞자리, 뒷 인터벌 뒷자리
        #  3) 뒷 인터벌이 앞 인터벌에 포함되거나 (앞 인터벌 정렬 기준) -> 앞 인터벌 놔두고 뒷 인터벌 삭제

        #  +a) 최적화 작업!
        #  1) for 문 두 번 돌릴 필요 X -> 이미 정렬 완료!
        #  2) inter_cp 사용할 필요 X

         
        intervals.sort()
        idx = 0
        #inter_cp = intervals[:]
        while True:
            if idx >= len(intervals)-1:
                break
            nex = idx+1
            # case 2, 3
            if intervals[idx][1] >= intervals[nex][0]:
                # case 2
                if intervals[idx][1] <= intervals[nex][1]:
                    intervals[nex] = [intervals[idx][0], intervals[nex][1]]
                    intervals.remove(intervals[idx])
                
                # case 3
                else:
                    intervals[nex] = intervals[idx]
                    intervals.remove(intervals[idx])
            else:
                idx+=1
            #inter_cp = intervals[:]
         
        
        #for 문 제거 => 이미 정렬해준 상황이기에 필요 X    
        # for i in intervals:
        #     if i not in ans:
        #         ans.append(i)
        # ans.sort()
        
        return intervals

        '''
        solution 2
        시간 복잡도: O(NlogN) => by sort 함수 (아래 for문은 O(N))
        공간복잡도: O(N) => 새 공간 만들어서 거기에 계속 옮겨담는 형식

        merged = []
        intervals.sort()
        for i in intervals:
            if merged and merged[-1][1] >= i[0]:
                merged[-1][1] = max(merged[-1][1], i[1])
            else:
                merged.append(i)
        return merged
        '''