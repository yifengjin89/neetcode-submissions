# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        
        # 1. using slow fast pointer to find the mid point
        # 2. reverse right half 
        # 3. merge two list use l1, r1, l2, r2....
        
        # [0, 1, 2, 3,     4, 5, 6]
        # [0, 1, 2,        3, 4, 5]

        dummy = ListNode(0, head)
        new_head = dummy
        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        right_start = slow.next
        slow.next = None
        prev = None

        while right_start:
            next_ = right_start.next
            right_start.next = prev
            prev = right_start
            right_start = next_
        
        while prev:
            dummy.next = head
            head = head.next
            dummy = dummy.next

            dummy.next = prev
            prev = prev.next
            dummy = dummy.next
        
        dummy.next = head
