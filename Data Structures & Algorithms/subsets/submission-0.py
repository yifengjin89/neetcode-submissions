class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, res, [], 0)
        return res
    
    def dfs(self, nums, res, path, start):
        res.append(path[:])

        for i in range(start, len(nums)):
            path.append(nums[i])
            self.dfs(nums, res, path, i+1)
            path.pop()
        