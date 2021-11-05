class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            anagrams["".join(sorted(word))].append(word)
            # "".join(sorted(word)) => key
            # word => value

        return list(anagrams.values())