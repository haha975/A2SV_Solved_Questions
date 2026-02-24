class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        left=0
        right=len(people)-1
        ans=0
        while right>left:
            sum=people[left]+people[right]
            if sum<=limit:
                ans+=1
                left+=1
                right-=1
            else:
                ans+=1
                left+=1
        
        if left==right:
            ans+=1     
               
        return ans      
