class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # we could simply return nums + nums but this is solution is more understanding
        ans = [0] * (2 * len(nums))
        ind2 = len(nums)
        for i in range(len(nums)): 
            ans[i] = nums[i]
            ans[ind2] = nums[i]
            ind2 += 1

        return ans