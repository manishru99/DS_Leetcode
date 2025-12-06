# 846. Hand of Straights

# TC = O(nlogn)
# SC = O(n)
import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        # create hashmap to store key and its cnt
        count = {}
        for num in hand:
            count[num] = 1 + count.get(num, 0) # get the val at num key or default to 0 if it doesn't exist
        # create a heap with the key from the hash
        minH = list(count.keys()) # s converting the keys of the dictionary count into a list and storing it in minH.
        heapq.heapify(minH) # nlogn to create
        while minH: # nlogn - all N elements are processed
            # get the min val to start the grp
            first = minH[0]
            for i in range(first, first + groupSize):
                if i not in count:
                    return False # key doesn't exist
                count[i] -= 1 # if exists decrement the cnt
                if count[i] == 0:
                    # if cnt of i becomes 0 then it should be the min val of heap
                    if i != minH[0]:
                        return False
                    # if it's the min of heap then pop it from heap
                    heapq.heappop(minH)
        return True
        