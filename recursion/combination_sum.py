#39. Combination Sum

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #Backtracking
        ans = []
        ds = []
        def findCombination(ind: int, target: int):
            if ind == len(candidates):
                if target == 0:
                    ans.append(ds[:])
                return
            if candidates[ind] <= target:
                ds.append(candidates[ind])
                #take
                findCombination(ind, target - candidates[ind])
                ds.pop()
            #Not take
            findCombination(ind + 1, target)
        findCombination(0, target)
        return ans

'''
TC: O(2^t * k) where t is the target, k is the average length

Reason: Assume if you were not allowed to pick a single element multiple times, every element will have a couple of options: pick or not pick which is 2^n different recursion calls, also assuming that the average length of every combination generated is k. (to put length k data structure into another data structure)

Why not (2^n) but (2^t) (where n is the size of an array)?

Assume that there is 1 and the target you want to reach is 10 so 10 times you can “pick or not pick” an element.

SC: O(k*x), k is the average length and x is the no. of combinations
'''