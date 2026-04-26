class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hMap = {}
        for k,num in enumerate(nums):
            diff = target - num
            if diff in hMap.keys():
                return [hMap[diff], k]
            hMap[num]=k
        return[]
        