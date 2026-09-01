class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # we coudl make a set and simply return t,f depending on size

        chk = []
        for num in nums:
            if num in chk:
                return True
            chk.append(num)
        return False
        