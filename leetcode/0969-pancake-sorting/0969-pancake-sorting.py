class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans=[]
        n=len(arr)
        for x in range(n,1,-1):
            i=arr.index(x)

            if i==x-1:
                continue
            
            if i!=0:
                ans.append(i+1)
                arr[:i+1]=reversed(arr[:i+1])

            ans.append(x)
            arr[:x]=reversed(arr[:x])
        return ans

        
        