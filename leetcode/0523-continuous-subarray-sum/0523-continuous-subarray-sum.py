class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        prif=[]
        hash={0:-1}
        for i in range(len(nums)):
            if len(prif)==0:
                prif.append(nums[i])
            else:
                prif.append(prif[-1]+nums[i])
            p=prif[-1]%k
            if p not in hash:
                hash[p]=i
            elif p in hash:
                check=i-hash[p]
                print(check)
                
                if check>=2:
                    return True
        return False
        



        