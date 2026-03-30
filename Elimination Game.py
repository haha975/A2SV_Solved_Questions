class Solution:
    def lastRemaining(self, n: int) -> int:
        def du(n,left=True):
            if n==1:
                return 1
            half=n//2
            su=du(half,not left)
            if left:
                return 2*su
            else:
                if n % 2 == 0:
                    return 2 * su - 1
                else:
                    return 2 * su
        return du(n,left=True)
