class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        ans = [0] * (2 * len(nums))
        # we have to copy each into correct placy we have to also find a 2nd half 
        ind2 = len(nums)
        for i in range(len(nums)): 
            ans[i] = nums[i]
            ans[ind2] = nums[i]
            ind2 += 1
            
        return ans