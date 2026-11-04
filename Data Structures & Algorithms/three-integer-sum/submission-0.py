class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # This is a two pointers iteration problem.
        # First to sort the nums, then iterate through the nums. At each step, I fix the curr index as the 
        # first number, then place the left pointer at i + 1 and right pointer at the end of the numbers.
        # Then check if the sum is equal to 0, if is too larger, move the right pointer to left,
        # If is too small, move the left pointer to right. If equals 0, record the triplets.
        # Also skip duplicate values for the fixed index and also skip duplicates when moving the pointers.
        # Time complexity is O(n^2), space is O(1)
        if not nums:
            return []
        
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                return res
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.two_sum(nums, i, res)
        
        return res
    
    def two_sum(self, nums, curr_idx, res):
        left = curr_idx + 1
        right = len(nums) - 1
        while left < right:
            total = nums[curr_idx] + nums[left] + nums[right]
            if total > 0:
                right -= 1
            elif total < 0:
                left += 1
            else:
                res.append([nums[curr_idx], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
        