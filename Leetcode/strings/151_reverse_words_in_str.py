# 151 Reverse words in a string

class Solution:
    def reverseWords(self, s: str) -> str:
        '''
        # striver sol
        st = []
        s += " "
        word = ""
        for char in s:
            if char == " ":
                st.append(word)
                word = ""
            else:
                word += char
        rev_sent = " ".join(st[::-1])
        return rev_sent
        '''
        # 2nd solution
        # TC = O(n) SC = O(n)
        words = s.split()
        return " ".join(words[::-1])