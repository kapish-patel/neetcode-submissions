from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # we need a hash map to store letters and count of each letter
        sMap = Counter(s)
        tMap = Counter(t)

        return sMap == tMap