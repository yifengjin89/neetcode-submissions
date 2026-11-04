class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # we just need a hashset to store the array, once its visited, just return false
        visited = set()
        for num in nums:
            if num in visited:
                return True
            visited.add(num)
        
        return False
        