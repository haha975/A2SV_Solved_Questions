class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
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

        
        anss=[]
        for i in ans:
            i.sort()
            print (i)
            if i not in anss:
                anss.append(i)
        return anss
        