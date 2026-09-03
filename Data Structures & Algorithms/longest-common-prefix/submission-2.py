class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # sorting lexicographically
        length = len(strs)
        if length == 0:
            return ""

        if length == 1:
            return strs[0]

        strs = sorted(strs)

        for i in range(min(len(strs[0]), len(strs[-1]))):
            if strs[0][i] != strs[-1][i]:
                return strs[0][:i]
        return strs[0]
                
        