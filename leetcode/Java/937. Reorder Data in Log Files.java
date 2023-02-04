class Solution {
    public String[] reorderLogFiles(String[] logs) {
      // 풀이: Arrays.sort()에서 소트 방식을 lambda expression으로 커스텀한다.
      // 시간복잡도: O(nlogn) -> Array.sort()에서 Object 타입일 때 머지 소트 사용.
      // 공간 복잡도: O(n) -> 각 log마다 split한 log와 reorder한 log를 담아야 할 공간이 필요
        Arrays.sort(logs, (log1, log2) -> {
            String[] isSplit1 = log1.split(" ", 2);
            String[] isSplit2 = log2.split(" ", 2);
            boolean isDigit1 = Character.isDigit(isSplit1[1].charAt(0));
            boolean isDigit2 = Character.isDigit(isSplit2[1].charAt(0));
            if(!isDigit1 && !isDigit2) {
                int cmp = 0;
                // 1. identifier 제외하고 비교
                cmp = isSplit1[1].compareTo(isSplit2[1]);
                if (cmp != 0) return cmp;
                // 2. 모두 똑같다면 identifier 비교
                cmp = isSplit1[0].compareTo(isSplit2[1]);
            }
            // 둘다 Digit이면 비교할 필요 없음 -> 이미 relative order를 만족한다 했으므로. 
            // 그러니 둘다 digit이면 0을 뱉고 그렇지 않은 -> 한쪽만 digit인 경우에만 letter가 앞에 오도록 한다.
            return isDigit1 ? (isDigit2 ? 0 : 1) : -1;
        });
        return logs;

        // List<String> letterLogs = new ArrayList<>();
        // List<String> digitLogs = new ArrayList<>();
        // for (String log : logs) {
        //     int i=0;
        //     while(Character.isLetterOrDigit(log.charAt(i))) i++;
        //     if (Character.isLetter(log.charAt(i+1))) {
        //         letterLogs.add(log);
        //         continue;
        //     }
        //     digitLogs.add(log);
        // }
        // System.out.println("letterLogs");
        // letterLogs.forEach(System.out::println);
        // System.out.println("digitLogs");
        // digitLogs.forEach(System.out::println);
        // return logs;
    }

}
