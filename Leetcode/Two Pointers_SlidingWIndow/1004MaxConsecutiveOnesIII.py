# 1004. Max Consecutive Ones III

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        '''
        #Brute
        #TC = O(n^2)
        max_len = 0
        for i in range(n):
            zeroes = 0
            for j in range(i, n):
                if nums[j] == 0:
                    zeroes += 1
                if zeroes <= k:
                    #len of subarr
                    len1 = j - i + 1
                    #Update maxlen
                    max_len = max(max_len, len1)
        return max_len
        '''
        #Optimized 2 pointer, sliding window
        #TC = O(2n)
        #SC = O(1)
        '''
        Outer While Loop: The outer while loop runs while r < n. Since r is incremented in each iteration, the loop runs ( O(n) ) times.
Inner While Loop: The inner while loop runs only when zeroes > k. In the worst case, each element is processed twice: once by the outer loop and once by the inner loop. Therefore, the total number of operations is still ( O(n) ).
Combining these, the overall time complexity is: [ O(n) ]
        
        l, r = 0, 0
        maxlen = 0
        zeroes = 0
        while r < n:
            if nums[r] == 0: zeroes += 1
            #Make valid number of 0s if they exceed k
            while zeroes > k:
                if nums[l] == 0:
                    zeroes -= 1
                    l += 1
            #Update count if number of 0s less than k
            if zeroes <= k:
                len1 = r - l + 1
                maxlen = max(maxlen, len1)
            r += 1
        return maxlen
        '''
        #Best approach
        #TC = O(n)
        #SC = O(1)
        l, r = 0, 0
        maxlen = 0
        zeroes = 0
        while r < n:
            if nums[r] == 0: zeroes += 1
            #Now if 0s have exceeded k
            if zeroes > k:  #Change from prev approach
                if nums[l] == 0:
                    #Decrement 0s cnt
                    zeroes -= 1
                #Increment l every time (Shrink the window)
                l += 1
            #If 0s are less than = k then update len
            if zeroes <= k:
                len1 = r- l + 1
                maxlen = max(maxlen, len1)
            r += 1
        return maxlen
        
            

                

