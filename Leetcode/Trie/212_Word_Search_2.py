# 212. Word Search II

# Solution 1
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])  # Get dimensions of the board
        res = []  # List to store the found words

        def dfs(r, c, word, index, visited):
            # Base case: if we've matched all characters in the word
            if index == len(word):
                return True
            
            # Check for out-of-bound indices
            if not (0 <= r < rows and 0 <= c < cols):
                return False

            # If this cell is already visited in the current DFS path
            if vis[r][c]:
                return False
            
            # If current board character doesn't match the word at current index
            if board[r][c] != word[index]:
                return False
            
            # Mark current cell as visited
            vis[r][c] = True

            # Explore all 4 directions: up, down, left, right
            found = (
                dfs(r-1, c, word, index+1, visited) or
                dfs(r+1, c, word, index+1, visited) or
                dfs(r, c-1, word, index+1, visited) or
                dfs(r, c+1, word, index+1, visited)
            )

            # Backtrack: unmark the cell after exploring
            vis[r][c] = False
            return found

        # For each word, search for a path on the board that matches the word
        for word in words:
            found = False  # Flag to exit early if word is found
            for r in range(rows):
                for c in range(cols):
                    # Create a fresh visited matrix for this word attempt
                    vis = [[False] * cols for _ in range(rows)]

                    # If starting character matches, begin DFS
                    if board[r][c] == word[0] and dfs(r, c, word, 0, vis):
                        res.append(word)
                        found = True
                        break  # Break inner loop if word is found
                if found:
                    break  # Break outer loop if word is found

        return res  # Return all found words

# Solution 2
# Trie and DFS with backtracking

# TC = - Worst case: O(N * L + M * N * 4^L)
# SC = - O(N * L + L) → O(N * L) (since L is small relative to N)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        res = set()

        trie = Trie()
        for word in words:
            trie.insert(word)

        def dfs(r, c, node, vis):
            if node.word:
                res.add(node.word)
                node.word = None
            if not (0 <= r < rows and 0 <= c < cols):
                return 
            if board[r][c] not in node.children:
                return 
            vis[r][c] = True
            char = board[r][c]
            found = (
                dfs(r-1, c, node.children[char], vis) or
                dfs(r+1, c, node.children[char], vis) or
                dfs(r, c-1, node.children[char], vis) or
                dfs(r, c+1, node.children[char], vis)
            )
            vis[r][c] = False
            #return found
            # Trie optimization: Remove unused nodes
            if not node.children[char].children:
                del node.children[char]

        vis = [[False] * cols for _ in range(rows)]  
        for r in range(rows):
            for c in range(cols):
                
                dfs(r, c, trie.root, vis)
        return list(res)
    

# With comments

class TrieNode:
    def __init__(self):
        self.children = {}    # Maps characters to TrieNode children
        self.word = None      # Stores a complete word when it's the end node

class Trie:
    def __init__(self):
        self.root = TrieNode()  # Root of the Trie

    def insert(self, word):
        node = self.root
        for char in word:
            # Create a new TrieNode if char doesn't exist in the current node
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word  # Mark the end of a word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        res = set()  # To store found words without duplication

        trie = Trie()
        for word in words:
            trie.insert(word)  # Insert all words into the Trie

        def dfs(r, c, node, vis):
            # If this node contains a word, add to result and set to None to avoid duplicates
            if node.word:
                res.add(node.word)
                node.word = None

            # Check if (r, c) is out of board bounds
            if not (0 <= r < rows and 0 <= c < cols):
                return

            # Prune the path if current cell's char isn't in the current Trie node
            if board[r][c] not in node.children:
                return

            vis[r][c] = True  # Mark the cell as visited
            char = board[r][c]

            # Explore 4 adjacent directions
            found = (
                dfs(r-1, c, node.children[char], vis) or
                dfs(r+1, c, node.children[char], vis) or
                dfs(r, c-1, node.children[char], vis) or
                dfs(r, c+1, node.children[char], vis)
            )

            vis[r][c] = False  # Backtrack

            # Optional Trie pruning for optimization: remove the child if it's no longer useful
            if not node.children[char].children:
                del node.children[char]

        # Initialize a visited matrix
        vis = [[False] * cols for _ in range(rows)]

        # Start DFS from each cell in the board
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie.root, vis)

        return list(res)  # Convert result set to list before returning