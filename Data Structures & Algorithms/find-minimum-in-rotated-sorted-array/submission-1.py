class Solution:
    def findMin(self, nums: List[int]) -> int:
        #[1,2,3, 4,5,6]
        #[4,5,6, 1,2,3]
        
        #[2,3,4, 5,6,1]
        #[3,4,5, 6,1,2]

        #[4,5,0, 1,2,3]
        if len(nums) == 1:
            return nums[0]

        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[left] <= nums[mid]:
                if nums[mid + 1] <= nums[right]:
                    return min(nums[left], nums[mid + 1])
                else:
                    left = mid + 1
            else:
                right = mid
        
        

