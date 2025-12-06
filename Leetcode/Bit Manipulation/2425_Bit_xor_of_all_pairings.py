class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        #Brute force
        '''
        m, n = len(nums1), len(nums2)
        nums3 = []

        for i in range(m):
            for j in range(n):
                if nums1[i] != nums2[j]:
                    nums3.append(nums1[i] ^ nums2[j])
                else:
                    nums3.append(0)
        
        #Xor of all nos in nums3
        res = 0
        for num in nums3:
            res ^= num
        return res
        '''
        xor1, xor2 = 0,0

        #xor of nums1
        for num in nums1:
            xor1 ^= num

        #xor of nums2
        for num in nums2:
            xor2 ^= num

        res = 0
        #if nums2 length odd take nums1 and vice versa
        #Xor op cancel out if even num of elem
        if len(nums2) % 2 == 1: 
            res ^= xor1
        if len(nums1) % 2 == 1:
            res ^= xor2

        return res

#TC = O(len(nums1) + len(nums2))
#Sc = O(1)

