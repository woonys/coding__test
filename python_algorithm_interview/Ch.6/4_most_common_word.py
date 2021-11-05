class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        #1. my solution
        import collections, re
        paragraph = re.sub("\s+", ",", paragraph.strip())
        li = paragraph.lower().split(",")
        ans = []
        for i in li:
            i = re.sub(r'[^\w\s]','',i)
            if i == "":
                pass
            else:
                if i not in banned:
                    ans.append(i)

        counter = collections.Counter(ans)

        return counter.most_common(1)[0][0]
        #2. 답안
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
                 .lower().split()
                    if word not in banned]

        #개수를 담아두는 변수: 딕셔너리를 사용 => defaultdict()로 int 값이 자동으로 부여되게끔!
        # counts = collections.defaultdict(int)
        # for word in words:
        #     counts[word] +=1

        # or 그냥 most_common으로 처리!
        counter = collections.Counter(words)
        return counter.most_common(1)[0][0]

