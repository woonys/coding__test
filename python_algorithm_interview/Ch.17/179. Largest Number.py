'''
- How to solve?: 답안 (혼자 1시간 풀다가 실패)
- 접근 방식: 부동 소수점 계산
  처음에 부동 소수점으로 내려서 계산하면 될 것이라 판단.
  이러면 2가지 문제가 발생하는데
  1) 자릿수가 1인 수 처리 => 자릿수를 최대치로 올려서 해결
  2) 파이썬 부동 소수점 계산 문제 => round()로 해결


  3) 근데 반례를 보니까 단순히 자릿수가 1이라서 문제가 아님을 깨달음.
    반례: 1113, 111311
    내 풀이방식대로 하면 1113 < 111311이라 1113111113으로 배치하는데
    실제로 더 큰건 1113111311이었..
    단순히 크기 비교만으로는 해결이 되지 않음을 깨닫고 접음
- 시간 복잡도: O(NlogN) => sorting algorithm
- 공간 복잡도: O(1)

'''

# answer
# 두 값을 합쳐서 더 큰 값을 비교(여기서 더하는 건 실제로 값을 더하는 게 아니라 두 숫자를 합치는 것)
# ex) 12 + 3 => not 15, but 123 or 312

class Solution:
    def to_swap(self, n1: int, n2: int) ->bool:
            return str(n1) + str(n2) < str(n2) + str(n1)
        
    def largestNumber(self, nums: List[int]) -> str:
        
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and self.to_swap(nums[j-1], nums[j]):
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j -= 1
            i += 1
        return str(int(''.join(map(str, nums))))




# my solution
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        sorted_arr = []
        
        for num in nums:
            if 1  <= num < 10:
                num_cp = num
                cnt = 1
                while cnt != 11:
                    num += (num_cp)*(10**(-cnt))
                    cnt +=1
                num = round(num, 11)
            elif 10 <= num < 10**2:
                num *= 10**(-1)
                num = round(num, 2)
            elif 10**2 <= num < 10**3:
                num *= 10**(-2)
                num = round(num, 3)
            elif 10**3 <= num < 10**4:
                num *= 10**(-3)
                num = round(num, 4)
            elif 10**4 <= num < 10**5:
                num *= 10**(-4)
                num = round(num, 5)
            elif 10**5 <= num < 10**6:
                num *= 10**(-5)
                num = round(num, 6)
            elif 10**6 <= num < 10**7:
                num *= 10**(-6)
                num = round(num, 7)
            elif 10**7 <= num < 10**8:
                num *= 10**(-7)
                num = round(num, 8)
            elif 10**8 <= num < 10**9:
                num *= 10**(-8)
                num = round(num, 9)
            elif 10**9 <= num < 10**10:
                num *= 10**(-9)
                num = round(num, 10)
            
            sorted_arr.append(num)
            
        
        sorted_arr.sort(reverse=True) # 큰 순으로 정렬
        print(sorted_arr)
        #다시 꺼내기
        
        ans = ""
        for num in sorted_arr:
            number = str(num)
            leng = len(number)
            if leng >= 12:
                ans+=number[0]
            else:
                real_num = number[0] + number[2:]
                ans+=real_num
        return ans
                
            
        
                
        