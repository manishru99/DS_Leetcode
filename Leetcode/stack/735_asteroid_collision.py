
#735. Asteroid Collision

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #Solution 1
        #Solution 1 by simulation
        
        #TC = O(n**2)
        #SC = O(1)
        '''
        i = 0
        while i < len(asteroids)-1:
            #curr +ve and next is -ve
            if asteroids[i]>0 and asteroids[i+1] <0:
                #curr is larger than next
                if asteroids[i] > abs(asteroids[i+1]):
                    asteroids.pop(i+1)
                #curr is smaller than next
                elif asteroids[i] < abs(asteroids[i+1]):
                    asteroids.pop(i)
                    if i>0:    #handled -ve
                        i -= 1
                #both are equal
                else:
                    asteroids.pop(i)
                    asteroids.pop(i)
                    if i>0:  ##handled -ve
                        i -= 1
            else:
                i+=1
        return asteroids
        '''

        #Solution 2
        #TC = O(n)
        #Or specific TC=O(2n) as while loop will pop max n elem throughout the journey
        #st/list stores n elem which are popped 
        #SC = O(n)
        st = []
        n = len(asteroids)
        for i in range(n):
            #+ve elem
            if asteroids[i] > 0: st.append(asteroids[i])
            #-ve elem
            else:  
                #st top is +ve and top < abs(curr) 
                while st and st[-1] > 0 and st[-1] < abs(asteroids[i]):
                    st.pop()
                #st top is equal
                if st and st[-1] == abs(asteroids[i]):
                    st.pop()
                #st empty or top is -ve
                #no collision so just push
                elif not st or st[-1] < 0:
                    st.append(asteroids[i])
        return st


