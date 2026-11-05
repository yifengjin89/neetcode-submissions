class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        counter = Counter(t)
        left, matched = 0, 0
        start = 0
        min_sub_size = float('inf')
        min_sub = ""

        for right in range(len(s)):
            char = s[right]
            if char in counter:
                counter[char] -= 1
                if counter[char] >= 0:
                    matched += 1

            while matched == len(t):
                sub_size = right - left + 1
                if sub_size < min_sub_size:
                    min_sub_size = sub_size
                    start = left
                
                if s[left] in counter:
                    counter[s[left]] += 1
                    if counter[s[left]] > 0:
                        matched -= 1
                
                left += 1
        
        return "" if min_sub_size == float('inf') else s[start:start + min_sub_size]