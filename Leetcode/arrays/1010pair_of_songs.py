#1010. Pairs of Songs With Total Durations Divisible by 60

def numPairsDivisibleBy60(time):
    # Array to count occurrences of each remainder
    remainder_count = [0] * 60
    count = 0
    
    for t in time:
        remainder = t % 60
        # Find the complement remainder that would sum to a multiple of 60
        complement = (60 - remainder) % 60
        # Add the number of songs with the complement remainder to the count
        count += remainder_count[complement]
        # Increment the count of the current remainder
        remainder_count[remainder] += 1
    
    return count

# Example usage
time = [30, 20, 150, 100, 40]
print(numPairsDivisibleBy60(time))  # Output: 3

'''
Explanation
Remainder Calculation: For each song duration, calculate remainder = t % 60.
Complement Calculation: The complement remainder is (60 - remainder) % 60.
Count Pairs: For each song, add the number of songs with the complement remainder to the count.
Update Remainder Count: Increment the count of the current remainder.
This approach ensures that we efficiently count the pairs of songs whose total duration is divisible by 60.
'''
