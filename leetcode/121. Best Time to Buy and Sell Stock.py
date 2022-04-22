'''
Runtime: 1282 ms, faster than 56.79% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 25.1 MB, less than 8.26% of Python3 online submissions for Best Time to Buy and Sell Stock.

시간복잡도: O(n) -> for문 한 번만 돌면서 min_price와 max_profit 모두 갱신
공간복잡도: O(1) -> max_profit과 min_price만 갱신
'''

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
    
        # my Solution => TLE...
        # max_ans = 0
        # for i in range(len(prices)-1):
        #     other = prices[i+1:]
        #     cand = prices[i]
        #     max_other = max(other)
        #     if max_other - cand > max_ans:
        #         max_ans = max_other - cand
        # return max_ans