class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = [False] * len(nums)
        res = []
        self.dfs(nums, res, [], used)
        return res
    
    def dfs(self, nums, res, path, used):
        if len(path) == len(nums):
            res.append(path[:])
            return
        
        for i in range(len(nums)):
            if used[i]:
                continue
            
            used[i] = True
            path.append(nums[i])
            self.dfs(nums, res, path, used)
            used[i] = False
            path.pop()
        
        