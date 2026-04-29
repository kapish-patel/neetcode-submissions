class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupsMap = defaultdict(list)

        for srt in strs:
            sorte = ''.join(sorted(srt))
            groupsMap[sorte].append(srt)
        
        return list(groupsMap.values())
