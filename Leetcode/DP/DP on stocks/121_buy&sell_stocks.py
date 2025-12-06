# 121. Best Time to Buy and Sell Stock

# Optimized 
# TC = O(n) SC = O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if(not prices or n<2):
            return 0
        #We remember the past value (min price) so this is DP
        max_p = 0
        min_p = prices[0]
        
        for p in prices[1:]:
            if(p < min_p):
                min_p = p
            else:
                max_p = max(max_p, p - min_p)
        return max_p
        '''
# Brute 

        #b -> buy, s -> sell
        for b in range(0, n-1):
            diff = []
            for s in range(b+1, n):
                if(prices[s] > prices[b]):
                    diff.append(prices[s] - prices[b])
            maxp.append(max(diff))
        return max(maxp)

# Brute 2
# TC = O(n^2) SC = O(1)
#Or
#TC = O(n^2)
#SC = O(1)
for b in range(0, n-1):
    for s in range(b+1, n):
        if(prices[s] > prices[b]):
            maxp = max(prices[s]-prices[b], maxp)
return maxp
'''
        