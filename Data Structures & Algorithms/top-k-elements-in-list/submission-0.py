from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        count = dict(Counter(nums))
        arr = [[] for i in range(len(nums)+1)]
        for key, v in count.items():
            arr[v].append(key)

        for topk in range(len(arr)-1, 0, -1):
            for num in arr[topk]:
                result.append(num)
                if len(result) == k:
                    return result

            

            
        