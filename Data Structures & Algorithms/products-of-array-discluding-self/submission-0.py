class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0 for i in range(len(nums))]
        # prefix
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix = nums[i] * prefix
        
        # postfix
        postfix = 1
        for i in range(len(nums)-1, 0, -1):
            result[i] = postfix * result[i]
            postfix = nums[i] * postfix
        result[0] = postfix * result[0]
        return result
        