public class 121. Best Time to Buy and Sell Stock {
    class Solution {
        /* 
         * Runtime: 3 ms, faster than 71.47% of Java online submissions for Best Time to Buy and Sell Stock.
         * Memory Usage: 83.9 MB, less than 38.75% of Java online submissions for Best Time to Buy and Sell Stock.
         * 시간복잡도: O(n) -> for문 한 번으로 끝낸다.
         * 공간복잡도: O(1) -> 변수 두 개를 저장할 공간만 필요함.
         * 
        */
        

        public int maxProfit(int[] prices) {
            int minPrice = prices[0];
            int maxVal = 0;
            
            for (int i=1; i<prices.length; i++) {
                if ((prices[i] - minPrice) > maxVal) {
                    maxVal = prices[i] - minPrice;
                }
                if (prices[i] < minPrice) {
                    minPrice = prices[i];
                }
                
            }
            return maxVal;
        }
    }
}
