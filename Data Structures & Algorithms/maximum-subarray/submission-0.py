class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_sum = nums[0]
        curr_sum = 0

        # [2, -3, 4]

        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum < nums[i]:
                curr_sum = nums[i]

            max_sum = max(max_sum, curr_sum)

        return max_sum