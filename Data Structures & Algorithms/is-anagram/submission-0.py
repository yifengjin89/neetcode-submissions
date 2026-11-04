class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = {}
        for n in s:
            if n not in counter:
                counter[n] = 1
            else:
                counter[n] += 1
        
        for s in t:
            if s in counter:
                counter[s] -= 1
        
        for char in counter:
            if counter[char] > 0:
                return False
        

        return True

        