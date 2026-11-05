# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        #  0 <- 1 <- 2 <- 3
        prev = None
        while head:
            next_ = head.next
            head.next = prev
            prev = head
            head = next_
        
        return prev
        