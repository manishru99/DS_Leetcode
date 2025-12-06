# 68. Text Justification

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []                 # Final list of justified lines
        line, length = [], 0     # Current line's words and total character count (excluding spaces)
        i = 0                    # Pointer to iterate through words

        while i < len(words):
            # Check if adding the next word exceeds maxWidth 
            # (we add len(line) to account for one space between each word added so far)
            # Here for current i we are just checking if that word if added would exceed the maxwidth
            # If exceeds the don't add but justify the current contents
            if length + len(line) + len(words[i]) > maxWidth:
                # Line is full — time to justify it

                extra_space = maxWidth - length            # Total space to distribute
                slots = max(1, len(line) - 1)              # Space slots between words (1 if single word)
                spaces = extra_space // slots              # Evenly distributed base space
                remainder = extra_space % slots            # Leftover spaces to distribute to the leftmost slots

                for j in range(slots):
                    line[j] += " " * spaces                # Add base spaces
                    if remainder:
                        line[j] += " "                     # Add extra space to this slot if remainder left
                        remainder -= 1

                res.append("".join(line))                  # Join the words into one line and add to result
                line, length = [], 0                       # Reset for next line

            # Add current word to the line
            line.append(words[i])
            length += len(words[i])
            i += 1

        # Handle last line — left-justified with spaces at the end
        last_line = " ".join(line)                         # Single space between words
        trail_space = maxWidth - len(last_line)            # Remaining space to pad at the end
        res.append(last_line + " " * trail_space)          # Pad the end with trailing spaces

        return res
    
'''
✂️ length
- This is the total number of characters in the words currently in the line.
- It does not count any spaces between them — just raw word lengths.
➕ len(line)
- This tells us how many words we’ve already added to the line.
- Since we’ll need one space between each of them, this gives the minimum number of spaces needed so far.
➕ len(words[i])
- This is the length of the next word we want to try placing on the current line.

For Handle last line logic
In the while loop, we only finalize a line when adding the next word would exceed maxWidth. So if all remaining words fit within the limit (as they often will on the last line), the loop just keeps accumulating them — but never triggers the justification logic inside that if block.
So by the time we exit the loop:
- line contains the leftover words that never breached maxWidth
- These words make up the last line, which should be left-justified (not fully justified)
That’s why we do this after the loop:

'''