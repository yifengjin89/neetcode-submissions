class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = set(nums)
        longest = 1
        for n in nums:
            if n - 1 not in nums:
                curr = 1
                while n + 1 in nums:
                    curr += 1
                    longest = max(longest, curr)
                    n += 1

        return longest
        