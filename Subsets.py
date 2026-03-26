class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backt(i ,arr):

            if i == len(nums):
                ans.append(arr[:])
                return

            arr.append(nums[i])
            backt(i+1,arr)
            
            arr.pop()
            backt(i+1,arr)
        backt(0,[])
        return ans
