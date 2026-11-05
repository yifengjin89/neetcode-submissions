class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        #[1,2,3, 4,5,6]
        #[2,3,4, 5,6,1]
        #[3,4,5, 6,1,2]
        #[4,5,6, 1,2,3]
        #[5,6,1, 2,3,4]
        #[6,1,2, 3,4,5]

        while left < right:
            mid = (left + right) // 2

            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if nums[mid+1] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid

        return left if nums[left] == target else -1
            

            
