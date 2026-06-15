class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        count = Counter(nums)
        print(count)
        arr = [[] for i in range(len(nums)+1)]

        for key, value in count.items():
            arr[value].append(key)


        for i in range(len(arr)-1, 0, -1):
            for num in arr[i]:
                result.append(num)
                if len(result) == k:
                    return result