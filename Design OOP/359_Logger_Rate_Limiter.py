# 359. Logger Rate Limiter

'''
Naive Solution:
We can store a list of all previous (timestamp, message) pairs. 
In each call, we loop through the list to get the most recent 
time message was logged and check if it was within 10 seconds of timestamp. 
Let n be the number of times shouldPrintMessage is called. 
Checking through the list takes O(n), so we take O(n^2) in total. 
Our list has size n, taking O(n) space. 
This is fast enough, but we can do better.
'''

# Optimal
'''
We use a hashmap that maps messages to their most recent timestamps. 
Retrieving/assigning hashmap[message] takes 
O(1), so we take O(n) in total. 
We also take O(n) space (in the worst case, every message is different, 
so all of them need to be inserted into the hashmap).
'''
class Logger:
    def __init__(self):
        # Dictionary to track the last printed timestamp for each unique message
        self.lastTime = dict()  # Key: message, Value: last printed timestamp

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # Check if message has been printed before and is within 10 seconds
        if message in self.lastTime and timestamp - self.lastTime[message] < 10:
            return False  # Not enough time has passed — suppress the message

        # Either message is new or enough time has passed — update the timestamp
        self.lastTime[message] = timestamp
        return True  # Message should be printed
    
'''
🔁 shouldPrintMessage(timestamp, message)
This method does the following:
- Checks if the message exists in the hash map.
- If yes, it checks the time difference.
- If allowed, it updates the hash map.
All of these operations are dictionary operations, which are on average:
- Time Complexity:
O(1) — Dictionary lookups, insertions, and deletions are constant-time operations in Python due to underlying hash table implementation.

🧠 Space Complexity
- The space used is proportional to the number of unique messages stored in self.lastTime.
- So in the worst-case, where all messages are unique and occur at intervals ≥ 10 seconds apart (so none get discarded), the space is:
- O(N), where N is the number of unique messages.

'''