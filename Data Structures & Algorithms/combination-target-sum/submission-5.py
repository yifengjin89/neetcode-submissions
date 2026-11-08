class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        self.dfs(nums, target, res, [], 0)
        return res
    
    def dfs(self, nums, target, res, path, index):
        if target == 0:
            res.append(path[:])
            return
        

        
        for i in range(index, len(nums)):
            if target - nums[i] < 0:
                return
            
            path.append(nums[i])
            self.dfs(nums, target - nums[i], res, path, i)
            path.pop()
        