class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left=0
        right=len(skill)-1
        sum=skill[right]+skill[left]
        cham=0
        while right>left:
            if skill[left] + skill[right] != sum:
                return -1
            
            cham+=skill[left]*skill[right] 
            left+=1
            right-=1
        return cham


        
        
