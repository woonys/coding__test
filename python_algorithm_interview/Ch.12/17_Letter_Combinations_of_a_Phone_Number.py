from string import ascii_lowercase
from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {2: "abc", 3:"def", 4:"ghi", 5:'jkl', 6: "mno", 
              7: "pqrs", 8: "tuv", 9:"wxyz"}
        
        digit_list = list(map(int, digits)) # [2, 3]
        if digit_list == []:
            return digit_list
        iter_list = []
        for i in digit_list:
            iter_list.append(dic[i]) # [a, b, c], [d, e, f]
        
        ans_list = product(*iter_list)
        ans = []
        for i in ans_list:
            a = "".join(i)
            ans.append(a)
        return ans