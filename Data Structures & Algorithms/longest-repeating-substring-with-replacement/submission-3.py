class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # {A:3}
        # {A:3, B:1}
        # {A:4, B:1,}
        # {A:4, B:2,}
        if not s:
            return 0

        # s="AABABBA" k=1


        hashmap = defaultdict(int)
        left = 0
        longest = 1
        for right in range(len(s)):
            hashmap[s[right]] += 1
           
            while right - left + 1 - max(hashmap.values()) > k:
                hashmap[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)
            

        return longest