class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        char2idx = {}
        for i in range(len(s)):
            char2idx[s[i]] = i
        
        left = 0
        res = []
        longest = 0
        curr = 0
        for right in range(len(s)):
            curr = char2idx[s[right]]
            longest = max(longest, curr)
            if right == longest:
                res.append(right - left + 1)
                left = right + 1
                longest = 0

        return res