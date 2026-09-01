class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # simply use nested loop starting with next element in inner loop
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return sorted([i, j])
        # return sorted([i, j])

        # solution 2  - use less memory
        hmap = {}
        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in hmap.keys():
                print(hmap)
                return [hmap[diff], i]
            hmap[nums[i]] = i 
        return [0,0]
