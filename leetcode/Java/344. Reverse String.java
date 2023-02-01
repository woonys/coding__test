class Solution {
    public void reverseString(char[] s) {
        
        //시간 복잡도: O(N) (N/2)
        //공간 복잡도: O(1)
        // char 하나 선언해서 여기에 복사해놓고 두 값을 바꿔치기함.
        int count = s.length;
        for (int i =0; i < count/2; i++) {
            char c = s[i];
            s[i] = s[count-i-1];
            s[count-i-1] = c;
        }
    }
}
