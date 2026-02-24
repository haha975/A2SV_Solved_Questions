class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        ma=0
        while  left<right:
            width=right-left
            mi=min(height[left],height[right])
            
            ma=max(ma,width*mi)
            if height[left]<=height[right]:
                left+=1
            else:
                right -= 1
        return ma

        
