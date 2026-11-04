class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        seen = set()
        left = 0
        longest = 1

        # abc bde

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            longest = max(longest, right - left + 1)

        return longest