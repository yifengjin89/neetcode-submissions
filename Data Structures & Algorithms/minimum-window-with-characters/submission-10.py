class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = Counter(t)
        min_sub = float('inf')
        left = 0
        match = 0

        for right in range(len(s)):
            if s[right] in counter:
                counter[s[right]] -= 1
                if counter[s[right]] >= 0:
                    match += 1
            
            while match == len(t):
                if right - left + 1 < min_sub:
                    min_sub = right - left + 1
                    start = left
                
                if s[left] in counter:
                    counter[s[left]] += 1
                    if counter[s[left]] > 0:
                        match -= 1

                left += 1

        
        return "" if min_sub == float('inf') else s[start: start + min_sub]