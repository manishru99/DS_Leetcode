'''
// PROBLEM :- https://leetcode.com/problems/online-stock-span/

// LEETCODE | MEDIUM | MONOTONIC STACK

// Logic :- 
// Insert the current price and no of days encountered by the current price in the stack.
// In getting a future value, first check if that value is greater than top elements from the stack. 
// If yes, pop that and add those days to this current days. Repeat until the top of stack is greater than current price.

// Such a stack is referred to as monotonic stack.
'''
class StockSpanner:
    #Brute
    '''
    def __init__(self):
        self.prices = []  #This list defined globally under the stock spanner class

    def next(self, price: int) -> int:
        self.prices.append(price)
        span = 1
        for i in range(len(self.prices)-2, -1, -1):  #start from prev day's price
            if self.prices[i] <= price:
                span += 1
            else:
                break
        return span
    '''
        #The first entry [] initializes the StockSpanner object.
#Each subsequent entry [price] calls the next method with the given price and calculates the span based on the prices seen so far.
#TC= O(num of days) (Every time next function is taking num of days time for each entry)
#SC = O(total num of next calls)
    
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

#Optmized

        curr_days = 1
        while self.stock and self.stock[-1][0] <= price:
            curr_days += self.stock.pop()[1]
        self.stock.append((price, curr_days))
        return curr_days