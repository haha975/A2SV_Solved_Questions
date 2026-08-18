# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        coun=0
        cur=head
        while cur:
            coun+= 1
            cur = cur.next
        cur=head
        midd=coun//2
        for _ in range(midd):
            cur=cur.next
        return cur
            
        


                
