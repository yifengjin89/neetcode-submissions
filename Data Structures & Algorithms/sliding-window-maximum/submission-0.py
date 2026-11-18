class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        left = 0
        max_val = float('-inf')
        res = []
        hashmap = defaultdict(int)

        for right in range(len(nums)):
            hashmap[nums[right]] += 1

            if right - left + 1 >= k:
                max_val = max(hashmap)
                res.append(max_val)
                hashmap[nums[left]] -= 1
                if hashmap[nums[left]] == 0:
                    del hashmap[nums[left]]
                left += 1
        
        return res