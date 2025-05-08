# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []

        q = deque([(root,0)])
        cols = defaultdict(list)

        min_col, max_col = 0, 0

        while q:
            node, col = q.popleft()
            min_col = min(min_col, col)
            max_col = max(max_col, col)

            cols[col].append(node.val)

            if node.left:
                q.append((node.left, col - 1))
            if node.right:
                q.append((node.right, col + 1))

        return [cols[c] for c in range(min_col, max_col + 1)]
