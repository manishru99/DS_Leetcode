# 860. Lemonade Change

# TC = O(n) SC = O(1)

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        n = len(bills)
        five, ten = 0, 0
        # No need to take 20 as we won't count it
        for i in range(n):
            if bills[i] == 5: five += 1
            elif (bills[i] == 10):
                if five: 
                    five -= 1
                    ten += 1
                else: return False
            else: # given is 20
                if ten and five:
                    ten -= 1
                    five -= 1
                elif (five >= 3):
                    five -= 3
                else:
                    return False
        return True



