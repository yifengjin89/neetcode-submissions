class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []

        # [1, 2, 3] -> [3]
        # [3, 2, 1] -> [3, 2, 1]
        # [1, 3, 2] -> [3, 2]

        for i in range(len(nums)):
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            q.append(i)
            # 0,   i = 4, k= 3
            # out of bound/out of dated data, 
            if q[0] <= i - k:
                q.popleft()

            if i >= k - 1:
                res.append(nums[q[0]])
        
        return res