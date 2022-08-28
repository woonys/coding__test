class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> store = new HashMap<>();
        int[] ans = new int[2];
        for (int i=0; i< nums.length; i++) {
            int val = nums[i];
            int another = (target - val);
            if (store.containsKey(another)) {
                ans[0] = i;
                ans[1] = (int) store.get(another);
                return ans;
            } else {
                store.put(val, i);
            }
        }
        
        return ans;
    }
}