class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        whole=nums1+nums2
        whole.sort()
        left=0
        right=len(whole)-1
        if len(whole)%2==1:
            mid=(right+left)//2
            return whole[mid]
        else:
            mid=(right+left)//2
            mi=(whole[mid]+whole[mid+1])/2
            return mi


        