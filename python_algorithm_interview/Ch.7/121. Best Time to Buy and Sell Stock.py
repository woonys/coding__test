'''
How to solve: 답안 참고
시간복잡도: O(n) -> for문 1번으로 해결 / min, max 둘다 O(1)
공간복잡도: O(1) -> in-place
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        for price in prices:
            max_profit, min_price = 0, float('inf')
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit

# my solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        for price in prices:
            if price - min_price > max_profit:
                max_profit = price - min_price
            if min_price > price:
                min_price = price
        return max_profit
        
        
        
        
        
        # length = len(prices)
        # max_val = 0
        # for i in prices:
        #     idx = prices.index(i)
        #     for j in prices[idx+1:]:
        #         if j-i <0:
        #             continue
        #         max_val = max(j-i, max_val)
        # return max_val
                
                    
                
            
            
            