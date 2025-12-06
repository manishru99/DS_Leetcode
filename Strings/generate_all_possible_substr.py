# Generate all possible substrings of a given string

def all_substrings(s):
    n = len(s)
    substr = []
    for i in range(n):
        for j in range(i+1, n+1):
            substr.append(s[i:j])
    return substr

s = "abc"
print(all_substrings(s))
# Output: ['a', 'ab', 'abc', 'b', 'bc', 'c']