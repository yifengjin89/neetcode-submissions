class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits

        additonal = 1
        digits[-1] = 0
        for i in range(len(digits) - 2, -1, -1):
            digits[i] += additonal
            if digits[i] == 10:
                digits[i] = 0
                additonal = 1
            else:
                additonal = 0
            
        if additonal == 1:
            return [1] + digits
        
        return digits
