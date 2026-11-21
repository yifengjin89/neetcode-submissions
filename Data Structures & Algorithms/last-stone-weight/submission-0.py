class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-n for n in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            x = -heapq.heappop(max_heap)
            y = -heapq.heappop(max_heap)

            if x == y:
                continue
            
            heapq.heappush(max_heap, -(x-y))
        
        return 0 if len(max_heap) == 0 else -max_heap[0]
