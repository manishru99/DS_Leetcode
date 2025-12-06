# 2410. Maximum Matching of Players With Trainers

#TC = O(nlogn + mlogm) SC = O(1)
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        # Greedy
        n = len(players)
        m = len(trainers)
        players.sort()
        trainers.sort()
        l, r = 0, 0
        while l < m and r < n:
            if players[r] <= trainers[l]:
                r += 1
            l += 1
        return r
            
