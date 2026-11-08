class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        self.dfs(nums, target, res, [], 0, 0)
        return res
    
    def dfs(self, nums, target, res, path, total, index):
        if total == target:
            res.append(path[:])
            return
        
        for i in range(index, len(nums)):
            total += nums[i]
            if total > target:
                return
            
            path.append(nums[i])
            self.dfs(nums, target, res, path, total, i)
            total -= nums[i]
            path.pop()
        
        