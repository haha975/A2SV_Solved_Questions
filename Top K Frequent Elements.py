class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        diff={}
        ans=[]
        for i in range(len(nums)):
            if nums[i] not in diff:
                diff[nums[i]]=1
            else:
                diff[nums[i]]+=1
        list1=list(diff.values())
        li=sorted(list1,reverse=True)
        for i in range(k):
            for key,value in diff.items():
                 if value==li[i]:
                    ans.append(key)
        return list(set(ans))

        

        


        


        
