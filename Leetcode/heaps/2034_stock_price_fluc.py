# 2034. Stock Price Fluctuation 

import heapq

class StockPrice:

    def __init__(self):
        self.prices = {}                 # hashmap timestamp -> price
        self.max_heap = []              # (-price, timestamp)
        self.min_heap = []              # (price, timestamp)
        self.latest_time = 0

    def update(self, timestamp: int, price: int) -> None:
        self.prices[timestamp] = price
        self.latest_time = max(self.latest_time, timestamp)
        heapq.heappush(self.max_heap, (-price, timestamp))
        heapq.heappush(self.min_heap, (price, timestamp))

    def current(self) -> int:
        return self.prices[self.latest_time]

    def maximum(self) -> int:
        # Lazy removal: pop until the top of heap is valid
        while True:
            price, timestamp = self.max_heap[0]
            if self.prices[timestamp] == -price:
                return -price
            heapq.heappop(self.max_heap)

    def minimum(self) -> int:
        while True:
            price, timestamp = self.min_heap[0]
            if self.prices[timestamp] == price:
                return price
            heapq.heappop(self.min_heap)


'''

 Data Structures Recap
- prices: Dict storing the latest price per timestamp → O(1) lookup
- max_heap and min_heap: Heaps storing potentially outdated entries
- latest_time: Tracks the max timestamp

⏱️ Time Complexity
update(timestamp, price)
- Dictionary update → O(1)
- heappush to both heaps → O(log n) each
- Total: O(log n) per update (since heap size grows with total updates n)
current()
- Just a dictionary lookup → O(1)
maximum() / minimum()
- Worst case: multiple heappop() calls to remove outdated entries.
- In the worst case, the top of the heap is invalid repeatedly
- But since each invalid heap entry is eventually removed once, the total cost is amortized across all operations
- Amortized Time: O(log n) per call

🧮 Space Complexity
- prices: stores one entry per timestamp → O(n)
- max_heap and min_heap: can have up to one entry per update (including outdated ones) → O(n)
- Total: O(n) space


Sure! Let’s walk through the logic behind the `StockPrice` class and how each method functions together:

---

### 💡 **Core Idea**

Since stock prices can be updated out of order and may be overwritten at the same timestamp, we need a way to:

- Track the **most recent price**
- Efficiently retrieve the **maximum and minimum** prices, even as updates occur
- Handle **updates that overwrite earlier entries**

---

### 🧱 **Data Structures Used**

1. **Dictionary `prices[timestamp] = price`**  
   - Holds the **latest price for each timestamp**
   - Ensures that if an existing timestamp is updated, we overwrite it

2. **Max-Heap `max_heap = [(-price, timestamp)]`**  
   - Stores all prices (negated) to simulate a **max-heap**
   - Might include outdated values, so we **validate** using the dictionary when retrieving

3. **Min-Heap `min_heap = [(price, timestamp)]`**  
   - Regular min-heap for minimum price queries
   - Also can have stale data → validated during retrieval

4. **Variable `latest_time`**  
   - Always tracks the **highest (latest) timestamp** seen so far
   - Used by `current()` to give the latest price

---

### ⚙️ **Method Logic**

#### `update(timestamp, price)`  
- Record the new price in `prices[timestamp]`
- Update `latest_time` if this timestamp is the most recent
- Push the new price to both min- and max-heaps, even if it overwrites a previous one
  - We don't remove old values yet — that happens lazily during retrieval

#### `current()`  
- Returns `prices[latest_time]`

#### `maximum()`  
- While the top of the max-heap is stale (doesn’t match `prices[timestamp]`), pop it
- Return the current valid max

#### `minimum()`  
- Same as above but for the min-heap

---

### 🧠 Why "Lazy Deletion"?

Because removing arbitrary elements from a heap efficiently is hard. Instead, we keep all entries in the heaps and **skip invalid ones** during queries. The dictionary acts as the truth source.

---

Let me know if you want to see a dry run or visualize how outdated values get skipped — it’s a satisfying watch in action 📊🔁.

'''