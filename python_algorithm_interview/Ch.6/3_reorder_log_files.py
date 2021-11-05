class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        let = []
        dig = []
        for log in logs:
            if log.split(" ")[1].isalpha():
                let.append(log)
            else:
                dig.append(log)
                #digit은 원래 log 순서대로라 더이상 건들지 X
            let.sort(key=lambda x: (x.split("")[1:], x.split(" ")[0]))
            return let + dig