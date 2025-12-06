#Solution rfr neetcode video
#394. Decode String
#Neetcode 75

class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        for i in range(len(s)): #O(len(s))
            if s[i] != ']':
                st.append(s[i])
            else:
                substr = ""
                while st[-1] != '[':
                    substr = st.pop() + substr  #Append at the front  IMPORTANT
                st.pop() #for '['

                k = ""
                while st and st[-1].isdigit(): #for checking if top is between (0 < char <= 9)
                    k = st.pop() + k  #for number, add it to the beginning to preserve the order
                st.append(int(k) * substr) #Mulitply and append to the st for further operation

        #Now st has list of substrings, it has characters we need so simply join them
        return "".join(st)
                
#TC = O(n)
#SC = O(n)
