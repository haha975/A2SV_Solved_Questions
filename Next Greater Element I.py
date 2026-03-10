class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        stack=[]
        hash={}
        for num in nums2:
            while stack and stack[-1]<num:
                hash[stack.pop()]=num
            stack.append(num)
        for num in stack:
            hash[num]=-1
        for i in nums1:
            ans.append(hash[i])

        return ans

        
