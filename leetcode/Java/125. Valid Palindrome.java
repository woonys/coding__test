class Solution {
    public boolean isPalindrome(String s) {
        // Solution 1: By using StringBuilder & Regex -> 매우 느린 편
        // Runtime: 665 ms (24.79%)
        // Memory: 43.6 MB (40.34%)
        String alphaNum = s.toLowerCase().replaceAll("[^a-zA-Z0-9]", "");
        StringBuilder sb = new StringBuilder();

        String palinStr = sb.append(alphaNum).reverse().toString();
        return alphaNum.equals(palinStr) ? true : false;
        
        // Solution 2: By using For & While
        // Runtime: 3 ms -> (97.37%) -> 시간복잡도: O(N^2)
        // Memory: 42.2 MB (92.32%)
    }
}
