# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev=None
        temp=head
        c=0
        while temp and temp.next:
            temp=temp.next.next
            c+=2
        c+=1
        mid=c//2
        temp=head
        for i in range(mid):
            prev=temp
            temp=temp.next
        if prev:
            prev.next=temp.next
            return head

        
