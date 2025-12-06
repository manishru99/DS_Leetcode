# 503. Next Greater Element II

#TC = O(4n)
#Sc = O(2n)

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nge = [-1]*n
        st = []
        for i in range(2*n-1, -1, -1):  #O(2n)
            #check st
            while st and st[-1] <= nums[i%n]:  #O(2n) As we push max 2n elem so pop 2n elem as shown for pop and append
                st.pop() #O(2n)
            if i < n:
                if st:
                    nge[i] = st[-1]
            st.append(nums[i%n])  #O(2n)
        return nge