class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hash={}
        for i in bills:
            if i not in hash:
                hash[i]=0
            hash[i]+=1
            if i==10:
                if 5 not in hash:
                    return False
                else:
                    hash[5]-=1
                    if hash[5]==0:
                        del hash[5]
            if i==20:
                if hash.get(10, 0) > 0 and hash.get(5, 0) > 0:
                    hash[10] -= 1
                    hash[5] -= 1

                    if hash[10] == 0:
                        del hash[10]
                    if hash[5] == 0:
                        del hash[5]
                elif hash.get(5, 0) >= 3:
                    hash[5] -= 3
                    if hash[5] == 0:
                        del hash[5]
                else:
                    return False
      

        return True


        
