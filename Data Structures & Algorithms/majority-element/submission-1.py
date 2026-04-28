import random
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # randomly pick a number check the count and return
        major = len(nums) // 2
        while True:
            num = random.choice(nums)
            if nums.count(num) > major:
                return num
        