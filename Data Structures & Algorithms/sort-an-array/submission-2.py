class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(arr, S, M, E):
            left = arr[S:M+1]
            right = arr[M+1 :E+1]
            i, j, k = S, 0, 0

            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1
            
            while j < len(left):
                arr[i] = left[j]
                j += 1
                i += 1
            
            while k < len(right):
                arr[i] = right[k]
                k += 1
                i +=1
            
            return arr


        def mergesort(nums, s, e):
            if s >= e:
                return nums
            m = (s + e) // 2
            mergesort(nums, s, m)
            mergesort(nums, m+1, e)
            return merge(nums, s, m, e)

        return mergesort(nums, 0, len(nums) -1)