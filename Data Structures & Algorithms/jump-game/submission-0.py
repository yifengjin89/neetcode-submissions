class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        
        max_reach = nums[0]

        for i in range(len(nums)-1):
            max_reach = max(max_reach, nums[i] + i)
            if i >= max_reach:
                return False

        return True 