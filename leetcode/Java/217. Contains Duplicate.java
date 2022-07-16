/**
Runtime: 6 ms, faster than 96.83% of Java online submissions for Contains Duplicate.
Memory Usage: 50.3 MB, less than 99.61% of Java online submissions for Contains Duplicate.

How to solve: My own solution

-   기존에 파이썬으로 풀었던 방식과 동일.
    자바에는 딕셔너리 대신 Map 인터페이스를 사용하기에
    HashMap 이용해서 기존 값과 동일한 게 있다면 Map에 추가해서 넣고 곧바로 return true

    처음 짰던 로직에서는 기존과 동일한 값이 있을 경우 Map에 값을 업데이트하고 true를 했는데
    굳이 이 로직 없이 곧바로 true를 리턴해도 괜찮기에 제거

    시간 복잡도: O(n) -> n은 nums의 원소 개수 -> for문 한 번으로 처리
    공간 복잡도: O(n) -> map에 들어갈 공간이 n칸 필요
 */

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i : nums) {
            Integer Int = new Integer(i);
            if (map.containsKey(Int)) {
                // Integer existValue = map.get(Int);
                // map.put(Int, existValue +1);
                return true;
            } else {
                map.put(Int, 1);
            }
        }
        return false;
    }
}