class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        hash={}
        for i in range(len(arr)-1):
            val=abs(arr[i]-arr[i+1])
            if val in hash:
                hash[val].append([arr[i],arr[i+1]])
            else:
                hash[val]=[[arr[i],arr[i+1]]]
        ans=[]
        for val,lis in hash.items():
            ans.append(val)
        c=min(ans)
        return hash[c]
        

        