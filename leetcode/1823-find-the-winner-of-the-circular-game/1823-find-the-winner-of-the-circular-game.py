class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def help(n,k):
            if n==1:
                return 0
            return (help(n-1,k)+k)%n
        return help(n,k)+1
            
            

        