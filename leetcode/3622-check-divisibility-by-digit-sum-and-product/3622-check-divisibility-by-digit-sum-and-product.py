class Solution:
    def checkDivisibility(self, n: int) -> bool:
        n=str(n)
        sum=0
        pro=1
        for i in range(len(n)):
            sum+=int(n[i])
            pro=pro*int(n[i])
        print(sum+pro)
        return int(n)%(sum+pro)==0
        

        