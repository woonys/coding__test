'''
How to solve: 답안 참고
시간 복잡도: O(N**2) => while & for 문
공간 복잡도: O(1) - in place


'''

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        result = 0
        #while 과 For 문을 함께 돌렸네
        while True:
            sub_count = 0
            
            #개수 순 추출
            for task, _ in counter.most_common(n+1):
                print("task is", task)
                sub_count += 1
                result +=1 
                print("counter bf", counter)
                counter.subtract(task)
                # 0 이하인 아이템을 목록에서 완전히 제거
                counter += collections.Counter()
                print("counter", counter)
            if not counter:
                break
            
            result += n - sub_count + 1
            print("result", result)
        return result