class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # This problem can be viewed as a two pointer probelm.
        # To solve it, Since its already sorted, I set up a left and right pointer at the beginng and end of the array list.
        # At each time, add up them to see if equals to the target, if greater than the target, move the right to left,
        # otherwise move the left pointer to right until equal the target.
        # The time complexicty is O(N), where n is the size of the array list because visit each element at most onec 
        # We don't use extra space so is O(1)
        if not numbers: return []
        res = []
        left, right = 0, len(numbers) - 1
        while left < right:
            sum_ = numbers[left] + numbers[right]
            if sum_ == target:
                return [left + 1, right + 1]
            if sum_ < target:
                left += 1
            else:
                right -= 1
        
        return []