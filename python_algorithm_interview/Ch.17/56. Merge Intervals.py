class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 총 세 가지 경우의 수: 
        # 1) 아예 안 겹치거나 => 패스
        # 2) 앞 인터벌 뒷자리와 뒤 인터벌 앞자리가 겹치거나 => 앞 인터벌 앞자리, 뒷 인터벌 뒷자리
        # 3) 뒷 인터벌이 앞 인터벌에 포함되거나 (앞 인터벌 정렬 기준) -> 앞 인터벌 놔두고 뒷 인터벌 삭제
        intervals.sort()
        idx = 0
        inter_cp = intervals[:]
        while True:
            if idx >= len(inter_cp)-1:
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
            inter_cp = intervals[:]
         
        ans = []
        
            
        for i in intervals:
            if i not in ans:
                ans.append(i)
        ans.sort()
        return ans