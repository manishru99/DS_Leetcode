class Solution:
    def countSetBits(self, num):
        cnt = 0
        for i in range(31, -1, -1):
            if num & (1<<i):
                cnt += 1
        return cnt
    
    def minimizeXor(self, num1: int, num2: int) -> int:
        cnt1 = self.countSetBits(num1)
        cnt2 = self.countSetBits(num2)
        res = 0

        #Cond 1
        if cnt1 == cnt2:
            return num1
        
        #cond2
        elif cnt1 < cnt2:
            res = num1
            cnt2 -= cnt1
            #Hint 2
            #If there are still left bits to set, try to set them from #the least significant bit
            for i in range(32):  #LSB to MSB
                if not (num1 & (1 << i)):  #If ith bit is not set
                    res += (1<<i)  #add 1 from LSB
                    cnt2 -= 1  #bits left to set
                    if cnt2 <= 0:  
                        break

        #cond 3
        else:
            #cnt1 > cnt2
            for i in range(31, -1, -1):  #MSB to LSB
                if num1 & (1<<i):   #If ith bit is set
                    res += (1<<i)  #add 1 from MSB 
                    cnt2 -= 1 #bits left to set
                    if cnt2 <= 0:
                        break
        return res
    
#TC = O(1)
#SC = O(1)


