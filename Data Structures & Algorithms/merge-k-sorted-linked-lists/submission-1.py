# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not any(lists):
            return None
        
        min_heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))
        
        dummy = ListNode()
        head = dummy

        while min_heap:
            val, i, node = heapq.heappop(min_heap)

            head.next = ListNode(val)
            head = head.next

            if node.next:
                node = node.next
                heapq.heappush(min_heap, (node.val, i, node))
        
        return dummy.next
            