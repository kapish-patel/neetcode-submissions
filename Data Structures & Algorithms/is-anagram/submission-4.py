from collections import Counter
# from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # use func 1 or 2 does the same thing
        # shmap = self.makeHmap(s)
        # thmap = self.makeHmap(t)

        # return shmap == thmap

        # 3rd solution - use Counter data structure
        shmap = Counter(s)
        thmap = Counter(t)
        return shmap == thmap
        
    
    # def makeHmap(self, srt: str) -> Dict:
    #     hmap = {}
    #     for s in srt:
    #         hmap[s] = hmap.get(s, 0) + 1
    #     return hmap

    # def makeHmap(self, srt: str) -> Dict:
    #     hmap = defaultdict(int)

    #     for s in srt:
    #         hmap[s] += 1
    #     return hmap

        