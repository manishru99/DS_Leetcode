# Nearer smaller element

#TC = O(2n)
#SC = O(n) + O(n)

def prevSmaller(A):
    #Approach 1: 2 for loops
    #Inside for loop will run from prev elem to 1st O(n^2)
    #Approach 2
    G = []
    st = []
    
    for num in A:
        while st and st[-1] >= num:
            st.pop()
        '''
        if st:  #Not empty
            G.append(st[-1])
        else:
            G.append(-1)
        '''
        G.append(st[-1] if st else -1)
        #Push curr in st
        st.append(num)
    return G
        