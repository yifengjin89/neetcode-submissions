class Solution:
    def jump(self, nums: List[int]) -> int:

        jump = 0
        max_reach = 0
        curr_reach = 0

        for i in range(len(nums)-1):
            max_reach = max(max_reach, nums[i] + i)

            if i == curr_reach:
                jump += 1
                curr_reach = max_reach

        return jump