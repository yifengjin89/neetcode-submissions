class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        count = Counter(t)
        left = matched = 0
        start, min_len = 0, float('inf')

        for right, char in enumerate(s):
            if char in count:
                count[char] -= 1
                if count[char] >= 0:
                    matched += 1

            while matched == len(t):
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                if s[left] in count:
                    if count[s[left]] == 0:
                        matched -= 1
                    count[s[left]] += 1

                left += 1

        return "" if min_len == float('inf') else s[start:start + min_len]