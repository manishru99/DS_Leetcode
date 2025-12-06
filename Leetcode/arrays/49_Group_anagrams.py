# 49. Group Anagrams

# Solution 2 Hashing
# TC = O(n * k) where n is the number of strings and k is the maximum length of a string.
# SC = O(n * k * 26) for the character count dictionary, where 26 is the number of lowercase letters.
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())

'''
This will group anagrams by their character count signature.
🔁 For each string in strs:

- "eat"
- count = [0]*26 → All zeros
- Process 'e', 'a', 't':
- 'e' → index 4 → count[4] += 1
- 'a' → index 0 → count[0] += 1
- 't' → index 19 → count[19] += 1
- count → [1, 0, 0, 0, 1, ..., 1 (at 19), ...]
- Key → tuple(count)
- Add to group:
res[(1,0,0,...)] = ["eat"]



- "tea"
- Same character frequencies as "eat" → same key
- Add to same group:
res[(1,0,0,...)] = ["eat", "tea"]



- "tan"
- 't' → 19, 'a' → 0, 'n' → 13
- count → [1, 0, ..., 1 (at 13), ..., 1 (at 19)]
- New key → added to its own group:
res[(1,0,...1 at 13...,1 at 19)] = ["tan"]



- "ate"
- Same letters as "eat"/"tea" → same key
- Add to group:
res[(1,0,...)] = ["eat", "tea", "ate"]



- "nat"
- Same letters as "tan" → same key
- Add to group:
res[...] = ["tan", "nat"]



- "bat"
- 'b' → 1, 'a' → 0, 't' → 19
- Unique key → new group:
res[...] = ["bat"]



✅ Final Result:
When we return list(res.values()), the order of groups can vary (since dictionaries are unordered), 
but the output will be:
[
  ["eat", "tea", "ate"],
  ["tan", "nat"],
  ["bat"]
]
'''

# SOlution 1
# TC = O(n * k logk) where n is the number of strings and k is the maximum length of a string.
# SC = O(n * k)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())

'''
- sorted(s) converts the string into a sorted list of characters.
- E.g., 'eat' → ['a', 'e', 't']
- ''.join(...) turns that sorted list back into a string key.
- So 'eat' → 'aet'
- res['aet'].append('eat'): group by this key.
✅ Any word that’s an anagram of 'eat' will also yield 'aet' as its sorted key—so they'll end up in the same list.

Dry Run on ["eat", "tea", "tan", "ate", "nat", "bat"]
| String | Sorted Key | Grouped Into | 
| "eat" | "aet" | ["eat"] | 
| "tea" | "aet" | ["eat", "tea"] | 
| "tan" | "ant" | ["tan"] | 
| "ate" | "aet" | ["eat", "tea", "ate"] | 
...

'''

