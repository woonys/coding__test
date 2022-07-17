import java.util.Arrays;


class Solution {
    public int maxSubArray(int[] nums) {
        
        //Solution 1: my solution
        /** 
        Runtime: 9 ms, faster than 5.84% of Java online submissions for Maximum Subarray.
        Memory Usage: 74.1 MB, less than 41.86% of Java online submissions for Maximum Subarray.

        시간복잡도: O(n) - 아래 나올 Solution 2와 동일한 시간복잡도이나 매번 dp 값을 갱신하기 위해 참조해야 하는 점에서 중간에 품이 들어가는 듯.
        공간복잡도: O(n) - dp array를 n개 원소만큼 생성해야 함
         */
        int length = nums.length;
        int[] dp = new int[length];
        dp[0] = nums[0];
        for (int i=1; i< length; i++) {
            dp[i] = nums[i] + (dp[i-1]>=0 ? dp[i-1] : 0);
        }
        int max = Arrays.stream(dp).max().getAsInt();
        return max;
        
        // Solution 2: Another solution from discuss - https://leetcode.com/problems/maximum-subarray/discuss/20211/Accepted-O(n)-solution-in-java
        
        /**
        Runtime: 2 ms, faster than 71.29% of Java online submissions for Maximum Subarray.
        Memory Usage: 73.7 MB, less than 52.41% of Java online submissions for Maximum Subarray.

        시간복잡도: O(n) - 기본적으로는 for문 한 번만 돌기 때문에 O(n)인 건 위와 동일하나 부가적인 로직이 없이 간단함.
        공간복잡도: O(1) - 위의 로직과 달리 dp array를 생성하지 않고 값을 갱신하는 구조.
         */
        int maxSoFar = nums[0], maxEndingHere=nums[0];
        for (int i=1; i< nums.length; ++i) { // 전위연산자: 작업 시작 전에 i 값 1 올리고 시작
            maxEndingHere = Math.max(maxEndingHere+nums[i],nums[i]);
            maxSoFar = Math.max(maxSoFar, maxEndingHere);
        }
        return maxSoFar;
        
        
    }
}