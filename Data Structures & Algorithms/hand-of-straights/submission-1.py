class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counter = Counter(hand)
        hand.sort()

        for num in hand:
            if counter[num] <= 0:
                continue
            
            for curr in range(num, num + groupSize):
                if counter[curr] == 0:
                    return False
                
                counter[curr] -= 1
        
        return True
