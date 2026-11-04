class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_zero = 0
        product = 1
        for num in nums:
            if num == 0:
                num_zero += 1
                continue
            product *= num 
        
        res = []
        if num_zero >= 2:
            return [0] * len(nums)

        for num in nums:
            if num_zero > 0:
                if num != 0:
                    res.append(0)
                else:
                    res.append(product)
            else:
                res.append(product // num)
        
        return res
        