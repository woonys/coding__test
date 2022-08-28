public class 350. Intersection of Two Arrays II {
    class Solution {
        public int[] intersect(int[] nums1, int[] nums2) {
            HashMap<Integer, Integer> map = new HashMap<>();
            List<Integer> ansList = new ArrayList<>();
            for (int i=0; i< nums1.length; i++) {
                if (map.containsKey(nums1[i])) {
                    int getVal = map.get(nums1[i]);
                    map.put(nums1[i], getVal + 1);
                } else {
                    map.put(nums1[i], 1);
                }
            }
            
            for (int i=0; i < nums2.length; i++) {
                if (map.containsKey(nums2[i]) && map.get(nums2[i]) >= 1) {
                    map.put(nums2[i], (map.get(nums2[i]) -1));
                    ansList.add(nums2[i]);
                }
            }
            
            int[] ans = ansList.stream().mapToInt(i->i).toArray();
            return ans;
            
        }
    }
}
