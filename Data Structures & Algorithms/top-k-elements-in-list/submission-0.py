class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_freq = Counter(nums)
        freq_list = [[] for _ in range(len(nums) + 1)]
        
        # num_to_freq {300:3, 200:2, 100:1}
        for key, val in num_to_freq.items():
            freq_list[val].append(key)
        

        res = []
        for i in range(len(freq_list) - 1, 0, -1):
            for num in freq_list[i]:
                res.append(num)
                if len(res) == k:
                    return res

        