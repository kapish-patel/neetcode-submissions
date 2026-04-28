from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majr = len(nums) // 2
        ctrmap = dict(Counter(nums))
        for k, v in ctrmap.items():
            if v >= majr:
                return k
        return 0
        