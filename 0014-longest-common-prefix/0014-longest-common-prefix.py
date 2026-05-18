class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for i in range(len(strs[0])):
            for w in range(len(strs)):
                if i == len(strs[w]) or (strs[w][i] != strs[0][i]):
                    return res
                
            res += strs[0][i]

        return res