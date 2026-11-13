class Solution:
    def isHappy(self, n: int) -> bool:
        
        total = 0
        seen = set()

        while True:
           
            while n:
                total += (n % 10) ** 2
                n //= 10
            
            
            if total == 1:
                return True
            if total in seen:
                return False
        
            seen.add(total)
            n = total
            total = 0
                
        