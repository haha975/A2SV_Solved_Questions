class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num)<=2:
            return False

        def back(first,second,remaning):
            if len(remaning)<max(len(first),len(second)):
                return False
            if (first[0]=="0" and len(first)!=1) or (second[0]=="0" and len(second)!=1):
                return False
            firs=int(first)
            sec=int(second)
            sum_both=str(firs+sec)
            lenn=len(sum_both)
            if len(remaning)<lenn:
                return False
            if sum_both==remaning[:lenn]:
                if lenn==len(remaning):
                    return True
                first=second
                second=sum_both
                remaning=remaning[lenn:]
                return back(first,second,remaning)
            

        i=0
        for j in range(i+1,len(num)):
            for k in range(j+1,len(num)):
                first=num[i:j]
                second=num[j:k]
                remaning=num[k:]
                if back(first,second,remaning):
                    return True
        return False
                

        