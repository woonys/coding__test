class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # anagrams = collections.defaultdict(list)

        # for word in strs:
        #     anagrams["".join(sorted(word))].append(word)
        #     # "".join(sorted(word)) => key
        #     # word => value

        # return list(anagrams.values())
    
        #my solution
        
        ans_list = []
        sort_list = []

        for i in strs:
            raw_str = i
            sorted_str = "".join(sorted(list(i)))

            if len(ans_list) == 0:
                sort_list.append(sorted_str)
                ans_list.append([raw_str])
                continue

            if sorted_str in sort_list:
                idx = sort_list.index(sorted_str)
                ans_list[idx].append(raw_str)
            else:
                sort_list.append(sorted_str)
                ans_list.append([raw_str])
    
        return ans_list