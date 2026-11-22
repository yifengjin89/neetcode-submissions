# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1


        carry = 0
        dummy = new_head = ListNode()

        while l1 or l2:
            a = 0 if not l1 else l1.val
            b = 0 if not l2 else l2.val

            total = a + b + carry
            if total > 9:
                carry = 1
                total -= 10
            else:
                carry = 0
            
            new_head.next = ListNode(total)
            new_head = new_head.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry > 0:
            new_head.next = ListNode(carry)
       
        return dummy.next










