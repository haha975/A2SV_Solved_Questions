class Solution:
    def isHappy(self, n: int) -> bool:
        li=[int(c) for c in str(n)]
        while True:
            if len(li)==1 and li[0]==1:
                return True
            elif len(li)==1 and li[0]!=1:
                if li[0] == 4:   
                    return False
            
            sum_digits = 0
            for j in range(len(li)):
                sum_digits += li[j] ** 2

            n = sum_digits  
            li = [int(c) for c in str(n)] 
                




        
