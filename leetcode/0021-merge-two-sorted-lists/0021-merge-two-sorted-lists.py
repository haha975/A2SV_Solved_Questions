# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list11=[]
        list22=[]
        def lis(list1):
            if list1:
                list11.append(list1.val)
                return lis(list1.next)
        def liss(list2):
            if list2:
                list22.append(list2.val)
                return liss(list2.next)
        lis(list1)
        liss(list2)
        cc=list11+list22
        cc.sort()
        c=ListNode(0)
        temp=c
        for i in range(len(cc)):
            temp.next=ListNode(cc[i])
            temp=temp.next

        return c.next

        