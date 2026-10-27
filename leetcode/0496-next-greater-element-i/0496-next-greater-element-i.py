class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        arr=[-1]*len(nums2)
        stack=[]
        for i in range(len(nums2)):
            
            while stack and nums2[stack[-1]]<nums2[i]:
                arr[stack.pop()] = nums2[i]
                
                
            stack.append(i)
        ans=[]
        for i in range(len(nums1)):
            ind=nums2.index(nums1[i])
            ans.append(arr[ind])
        print(stack ,arr)
        return ans
        
