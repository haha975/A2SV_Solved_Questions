class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        ans=0
        nu=str(num)
        check=nu[:k]
        if num%int(check)==0:
            ans+=1
        for i in range(k,len(nu)):
            check+=nu[i]
            check = check[1:]
            if int(check)==0:
                continue
            elif num%int(check)==0:
                ans+=1
        return ans


        