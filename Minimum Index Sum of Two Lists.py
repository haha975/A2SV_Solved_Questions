class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hashh={}
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i]==list2[j]:
                    c=i+j
                    hashh[list1[i]]=c
        cd = min(hashh.values())
        ans=[]
        for key,values in hashh.items():
            if values==cd:
                ans.append(key)
        return ans

        
