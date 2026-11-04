class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = defaultdict(list)
        for i in range(len(nums)):
            hashmap[nums[i]].append(i)
        
        for i in range(len(nums)):
            num = target - nums[i]
            if num in hashmap:
                indexs = hashmap[num]
                if nums[i] != num:
                    return [i, indexs[0]]
                else:
                    if len(indexs) > 1:
                        return [i, indexs[1]]
        
        return []
        