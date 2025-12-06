# 199. Binary Tree Right Side View

# Rfr Neetcode
# by DFS TC = O(n) SC = O(n)
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def dfs(node, depth):
            if not node:
                return
            if depth == len(ans):
                ans.append(node.val)  # First node at this depth
            dfs(node.right, depth + 1)  # Right first
            dfs(node.left, depth + 1)   # Then left

        dfs(root, 0)
        return ans
    
# by BFS TC = O(n) SC = O(n)
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        q = deque([root])
        while q:
            rightside = None
            qlen = len(q)
            for i in range(qlen):
                node = q.popleft()
                if node:
                    rightside = node
                    q.append(node.left)
                    q.append(node.right)
            # when for loop finishes for the current level and rightmost exists
            # then it is the rightmost node for that level
            if rightside:
                ans.append(rightside.val)
        return ans
    

# Left side view of the BT
'''
- BFS processes nodes level by level.
- The first non-null node encountered in each level is the leftmost visible node.
- You still enqueue children in left-to-right order, which preserves the left-first traversal
'''
class Solution:
    def leftSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        q = deque([root])
        while q:
            leftside = None
            qlen = len(q)
            for i in range(qlen):
                node = q.popleft()
                if node:
                    if leftside is None:
                        leftside = node  # First non-null node at this level
                    q.append(node.left)
                    q.append(node.right)
            if leftside:
                ans.append(leftside.val)
        return ans