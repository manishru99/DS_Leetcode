# 121. Best Time to Buy and Sell Stock

# TC = O(n) SC = O(1)
def maxProft(prices):
    n = len(prices)
    # edge
    if not prices or n <= 1:
        return 0
    min_price = prices[0]
    profit = 0
    for p in prices[1:]:
        if p < min_price:
            min_price = p
        else:
            profit = max(profit, p - min_price)
    return profit

'''
        #b -> buy, s -> sell
        for b in range(0, n-1):
            diff = []
            for s in range(b+1, n-1):
                if(prices[s] > prices[b]):
                    diff.append(prices[s] - prices[b])
            maxp.append(max(diff))
        return max(maxp)

        #Or
        #TC = O(n^2)
        #SC = O(1)
        for b in range(0, n-1):
            for s in range(b+1, n-1):
                if(prices[s] > prices[b]):
                    maxp = max(prices[s]-prices[b], maxp)
        return maxp
        
        
'''