class Solution:
    def findMin(self, nums: List[int]) -> int:
        #[1,2,3, 4,5,6]
        #[4,5,6, 1,2,3]
        
        #[2,3,4, 5,6,1]
        #[3,4,5, 6,1,2]

        #[4,5,0, 1,2,3]

        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]
        
        

