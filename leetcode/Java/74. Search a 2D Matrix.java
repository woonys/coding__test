public class 74. Search a 2D Matrix {

    /*
     * Runtime: 0 ms, faster than 100.00% of Java online submissions for Search a 2D Matrix.
     * Memory Usage: 42.7 MB, less than 53.51% of Java online submissions for Search a 2D Matrix.
     * 시간복잡도: O(logMN) -> 바이너리 서치 이용 & 전체 길이가 M*N인 하나의 sorted List에서 바이너리 서치를 한다고 생각하면 된다.
     * 공간 복잡도: O(1) -> 데이터 양에 따른 공간 증가가 없음. 상수.
     */
    class Solution {
        public boolean searchMatrix(int[][] matrix, int target) {
            // Exception case 정리
            if (matrix == null || matrix.length == 0) {
                return false;
            }
            // 값 설정
             
            int rows = matrix.length, cols = matrix[0].length;
            int start = 0;
            int end = rows * cols -1 ;
            
            while (start <= end) {
                int mid = (start + end) /2;
                // true case
                if (matrix[mid / cols][mid % cols] == target) {
                    return true;
                }
                if (matrix[mid / cols][mid % cols] < target) { // mid보다 target이 크다 -> start를 올려줘야 한다.
                    start = mid + 1;
                } else {
                    end = mid -1;
                }
            }
            return false;
        }
    }
    
}
