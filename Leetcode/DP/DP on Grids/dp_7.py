# DP 7 Striver Ninja's Training

# Recursion
class Solution:
    # Max merit points earned on arr that starts from 0 and ends at day
    # with last representing last task performed
    def f(self, day, last, task):
        """
        Recursive function to calculate the maximum merit points.

        :param day: Current day (0-indexed)
        :param last: Index of the task performed on the previous day (0, 1, 2), or 3 if no task was done yet
        :param task: 2D list of merit points for each task per day
        :return: Maximum merit points achievable from day 0 to 'day' without repeating tasks
        """
        # Base case: first day, choose any task except 'last'
        if day == 0:
            maxi = 0
            for i in range(3):
                if i != last:
                    maxi = max(maxi, task[0][i])
            return maxi

        maxi = 0
        # Try all tasks except the one done last
        for i in range(3):
            if i != last:
                # Choose task i today, and recurse for previous day with i as last
                points = task[day][i] + self.f(day - 1, i, task)
                maxi = max(maxi, points)

        return maxi

    def ninjaTraining(self, n, task):
        """
        Entry point to solve the Ninja's Training problem using recursion.

        :param n: Number of days
        :param task: 2D list where task[i][j] is the merit points for task j on day i
        :return: Maximum merit points achievable
        """
        # Start from last = 3 (no task done yet)
        return self.f(n - 1, 3, task)



'''
🧠 Time Complexity

In the recursive function `f(day, last)`:
- For each day, you try **3 tasks**, excluding the one done last.
- So for each `(day, last)` pair, you make up to **2 recursive calls** (since one task is excluded).

There are `n` days, and `last` can be `0`, `1`, `2`, or `3` (4 values).

But since there's **no memoization**, the recursion tree grows exponentially.

Worst-case Time Complexity: O(2^n)
- At each level of recursion (each day), you branch into up to 2 choices.
- So the total number of recursive calls grows exponentially with `n`.

🧠Space Complexity
- The maximum depth of the recursion stack is `n` (one call per day).
- No extra space is used beyond the call stack.

Space Complexity: O(n)
'''

