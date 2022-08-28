public class 88. Merge Sorted Array {
    /*
    Runtime: 0 ms, faster than 100.00% of Java online submissions for Merge Sorted Array.
    Memory Usage: 42.7 MB, less than 56.85% of Java online submissions for Merge Sorted Array.

    시간복잡도: O(n) -> 끝자리부터 출발해서 하나씩 비교 -> 이미 nums1, 2 둘다 정렬된 상태기 때문에 한번씩만 비교해도 가능
    공간복잡도: O(1) -> 주어진 nums가지고 끝냄.
     */
    class Solution {
        public void merge(int[] nums1, int m, int[] nums2, int n) {
            int tail1 = m-1, tail2 = n-1, fin = m+n-1;
            while (tail1 >=0 && tail2 >=0) {
                nums1[fin--] = (nums1[tail1] > nums2[tail2]) ? nums1[tail1--] : nums2[tail2--];
            }
            while (tail2 >= 0) {
                nums1[fin--] = nums2[tail2--];
            }
        }
    }
    
}
