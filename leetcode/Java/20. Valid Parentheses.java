public class 20. Valid Parentheses {
    class Solution {
        public boolean isValid(String s) {
            List<Character> arr = new ArrayList<>();
            for (int i=0; i < s.length(); i++) {
                char ch = s.charAt(i);
                if (arr.size() == 0) {
                    arr.add(ch);
                } else {
                    if (arr.get(arr.size()-1) == '[' && ch == ']') {
                        arr.remove(arr.size()-1);
                        continue;
                    }
                    if (arr.get(arr.size()-1) == '{' && ch == '}') {
                        arr.remove(arr.size()-1);
                        continue;
                    }
                    if (arr.get(arr.size()-1) == '(' && ch == ')') {
                        arr.remove(arr.size()-1);
                        continue;
                    }
                    arr.add(ch);
                }
            }
            if (arr.size() == 0) {
                    return true;
                } else {
                    return false;
                }
        }
    }
}
