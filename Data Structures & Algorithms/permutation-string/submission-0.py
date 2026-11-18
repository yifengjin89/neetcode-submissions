class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = Counter(s1)
        hashmap = defaultdict(int)
        left = 0

        for right in range(len(s2)):
            hashmap[s2[right]] += 1
            if right - left + 1 >= len(s1):
                if hashmap == counter:
                    return True

                hashmap[s2[left]] -= 1
                if hashmap[s2[left]] == 0:
                    del hashmap[s2[left]]
                    
                left += 1
        
        return False