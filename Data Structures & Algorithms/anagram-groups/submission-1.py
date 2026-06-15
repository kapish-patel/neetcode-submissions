class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}

        for s in strs:
            srt = ''.join(sorted(s))
            if srt not in hmap.keys():
                hmap[srt] = [s]
            else:
                hmap[srt].append(s)


        return list(hmap.values())
        