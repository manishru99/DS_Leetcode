# 567. Permutation in String

# Brute
# TC = O(n) * O(n) * O(nlogn) = O(n^3 logn)
# SC = O(n) In worst case substr size is whole of s2
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        for i in range(len(s2)):
            for j in range(i, len(s2)):
                substr = s2[i : j+1]
                substr = sorted(substr)
                if substr == s1:
                    return True
        return False
    
# Solution 2 using hashmap
# TC =  O(n² * k)
# SC = O(k)
'''- n = len(s2)
- k = len(s1) (or more precisely, the length of the window being checked)

- The outer loop runs n times (starting index i from 0 to n-1).
- The inner loop runs up to n - i times.
- Within the inner loop:
- Dictionary count2 is updated in O(1) time (since characters are assumed to be lowercase letters).
- The condition count1.get(s2[j], 0) < count2[s2[j]] is checked in O(1).
- However, building up count2 and tracking cur == need happens linearly per character, so for each iteration of the inner loop we potentially compare up to k characters before we break.
Worst case: for each i, the inner loop runs almost n times and does constant work per character ⇒ O(n²) overall.

- count1 stores character frequencies from s1 → O(k)
- count2 gets reset for each window in s2 → O(k) worst case if all unique characters in s1
✅ Space Complexity: O(k) (which is usually O(1) for fixed-size alphabets like lowercase English letters)
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        for c in s1:
            count1[c] = 1 + count1.get(c, 0)
        
        need = len(count1)
        for i in range(len(s2)):
            count2, cur = {}, 0
            for j in range(i, len(s2)):
                count2[s2[j]] = 1 + count2.get(s2[j], 0)
                if count1.get(s2[j], 0) < count2[s2[j]]:
                    break
                if count1.get(s2[j], 0) == count2[s2[j]]:
                    cur += 1
                if cur == need:
                    return True
        return False
    
# Solution 3 Sliding window

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Edge case: s1 can't be a permutation of any substring in s2 if it's longer
        if len(s1) > len(s2):
            return False

        # Initialize frequency arrays for s1 and initial window in s2
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1 # ord -> getting ASCII val of char 
            s2Count[ord(s2[i]) - ord('a')] += 1

        # Calculate how many characters currently match between s1Count and s2Count
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        # Start sliding the window in s2
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True  # All characters match → valid permutation found

            # Include new character at the right end of the window
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1

            # Update matches count based on new character impact
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            # Exclude character that's sliding out of the window (left end)
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1

            # Update matches based on removed character impact
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1

            # Move left boundary of the window forward
            l += 1

        # Check the final window after the loop
        return matches == 26
    
    
# Same as above but using hashmap in place of arr
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # If s1 is longer, no permutation is possible in s2
        if len(s1) > len(s2):
            return False

        # Count frequencies of each character in s1
        s1Count = {}
        for c in s1:
            s1Count[c] = s1Count.get(c, 0) + 1

        # Initialize frequency map for the first window in s2
        s2Count = {}
        for c in s2[:len(s1)]:
            s2Count[c] = s2Count.get(c, 0) + 1

        # Count how many characters match between s1Count and s2Count
        matches = 0
        for key in s1Count:
            if s1Count[key] == s2Count.get(key, 0):
                matches += 1

        l = 0  # Left boundary of the sliding window
        for r in range(len(s1), len(s2)):
            # If all characters match, permutation found
            if matches == len(s1Count):
                return True

            # Add the new character at the right end of the window
            char_in = s2[r]
            s2Count[char_in] = s2Count.get(char_in, 0) + 1

            # Adjust match count based on the inclusion of char_in
            if char_in in s1Count:
                if s2Count[char_in] == s1Count[char_in]:
                    matches += 1
                elif s2Count[char_in] == s1Count[char_in] + 1:
                    matches -= 1

            # Remove the character that's sliding out from the left
            char_out = s2[l]
            s2Count[char_out] -= 1
            if s2Count[char_out] == 0:
                del s2Count[char_out]  # Clean up zero-count keys

            # Adjust match count based on the removal of char_out
            if char_out in s1Count:
                if s2Count.get(char_out, 0) == s1Count[char_out]:
                    matches += 1
                elif s2Count.get(char_out, 0) == s1Count[char_out] - 1:
                    matches -= 1

            # Move the window forward
            l += 1

        # Final check after the loop completes
        return matches == len(s1Count)