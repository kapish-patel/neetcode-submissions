class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        l , r = 0, 0
        w1l = len(word1)
        w2l = len(word2)
        
        while l < w1l and r < w2l:
            res += word1[l]
            res += word2[r]

            l += 1
            r += 1

        if l != w1l:
            res += word1[l:w1l]
        
        if r != w2l:
            res += word2[l:w2l]
        
        return res