# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lis=[]
        stack=[]
        def help(head):
            if not head:   
                return
    
            lis.append(head.val)
            help(head.next)
        help(head)
        for i in range(len(lis)):
            if not stack or stack[-1]>lis[i]:
                stack.append(lis[i])
            else:
                while stack  and  stack[-1]<lis[i]:
                    stack.pop()
                stack.append(lis[i])
        
        

        dummy = ListNode(0)
        curr = dummy

        for val in stack:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next   

        