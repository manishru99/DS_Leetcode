#2081. Sum of k-Mirror Numbers

def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def to_base_k(n: int, k: int) -> str:
    res = ""
    while n > 0:
        res = str(n % k) + res
        n //= k
    return res

def k_mirror(k: int, n: int) -> int:
    def generate_palindromes():
        i = 1
        while True:
            # Odd-length palindrome
            s = str(i)
            yield int(s + s[-2::-1])
            # Even-length palindrome
            yield int(s + s[::-1])
            i += 1

    gen = generate_palindromes()
    count = 0
    total = 0

    while count < n:
        num = next(gen)
        if is_palindrome(to_base_k(num, k)):
            total += num
            count += 1

    return total

'''
High-Level Strategy
- Generate palindromes in base-10 (since these are relatively easy to construct and enumerate in order).
- For each one, convert it to base-k and check if it is also a palindrome in that base.
- Collect valid k-mirror numbers until we've found n, then return their sum.

🧠 Helper Functions
- A function to generate base-10 palindromes (both even and odd length).
- A function to convert a number to base-k and check if it’s a palindrome.

'''

# Correct code:

class Solution:
    def is_palindrome(self, s: str) -> bool:
        return s == s[::-1]

    def to_base_k(self, n: int, k: int) -> str:
        if n == 0:
            return "0"
        digits = []
        while n > 0:
            digits.append(str(n % k))
            n = n // k
        return ''.join(reversed(digits))

    def kMirror(self, k: int, n: int) -> int:
        count = 0
        total = 0
        length = 1  # Start with 1-digit numbers

        while count < n:
            # Generate palindromes of current length
            half_length = (length + 1) // 2
            start = 10 ** (half_length - 1)
            end = 10 ** half_length

            for num in range(start, end):
                s = str(num)
                if length % 2 == 0:
                    palindrome_str = s + s[::-1]
                else:
                    palindrome_str = s + s[:-1][::-1]
                palindrome = int(palindrome_str)
                # Check if palindrome in base k
                if self.is_palindrome(self.to_base_k(palindrome, k)):
                    total += palindrome
                    count += 1
                    if count == n:
                        return total
            length += 1

        return total