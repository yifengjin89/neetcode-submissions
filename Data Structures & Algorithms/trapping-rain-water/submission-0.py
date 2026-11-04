class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        max_height = max(height)
        max_height_idx = height.index(max_height)
        left_max = 0
        res = 0

        for i in range(max_height_idx):
            if height[i] > left_max:
                left_max = height[i]
            else:
                res += left_max - height[i]
        
        right_max = 0
        for i in range(len(height)-1, max_height_idx, -1):
            if height[i] > right_max:
                right_max = height[i]
            else:
                res += right_max - height[i]
        
        return res
        