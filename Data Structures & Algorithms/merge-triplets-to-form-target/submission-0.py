class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        r1 = False
        r2 = False
        r3 = False
        
        for a, b, c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            if a < target[0] and b < target[1] and c < target[2]:
                continue
            
            if a == target[0]:
                r1 = True
            if b == target[1]:
                r2 = True
            if c == target[2]:
                r3 = True
            
            if r1 and r2 and r3:
                return True
        
        return False

        