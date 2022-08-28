import java.util.PriorityQueue;
import java.util.Arrays;
import java.util.Collections;

public class 1464. Maximum Product of Two Elements in an Array {
    class Solution {
        public int maxProduct(int[] nums) {
            
            /* solution 1: sort 이용
            Runtime: 15 ms, faster than 5.27% of Java online submissions for Maximum Product of Two Elements in an Array.
            Memory Usage: 43.8 MB, less than 21.13% of Java online submissions for Maximum Product of Two Elements in an Array.
            
            시간복잡도: O(NlogN) -> Dual-pivot quick sort 사용
            */

            Integer[] list = Arrays.stream(nums).boxed().toArray(Integer[]::new);
            Arrays.sort(list, Collections.reverseOrder());
            int first = list[0];
            int second = list[1];
            return (first-1)*(second-1);

            /* Solution 2: priorityQueue 사용
            Runtime: 5 ms, faster than 24.67% of Java online submissions for Maximum Product of Two Elements in an Array.
            Memory Usage: 44.3 MB, less than 6.44% of Java online submissions for Maximum Product of Two Elements in an Array.
            */
            PriorityQueue<Integer> priorityQueue = new PriorityQueue<>(Collections.reverseOrder());
            for (int i=0; i < nums.length; i++) {
                priorityQueue.add(nums[i]);
            }
            int first = priorityQueue.poll();
            int second = priorityQueue.poll();
            return (first-1)*(second-1);  
        }    
    }
}
