from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # make a dictionary to keep track of each char or use a Counter data structure

        shmap = self.makeHmap(s)
        thmap = self.makeHmap(t)

        return shmap == thmap
        
    
    # def makeHmap(self, srt: str) -> Dict:
    #     hmap = {}
    #     for s in srt:
    #         hmap[s] = hmap.get(s, 0) + 1
    #     return hmap

    def makeHmap(self, srt: str) -> Dict:
        hmap = defaultdict(int)

        for s in srt:
            hmap[s] += 1
        return hmap

        