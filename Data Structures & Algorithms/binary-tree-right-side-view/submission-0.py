# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        results = []
        q = deque([(root, 0)])
        while q:
            curr_node, curr_level = q.popleft()
            if not curr_node:
                continue
            if len(results) < curr_level + 1:
                results.append(0)
            results[curr_level] = curr_node.val
            q.extend([(curr_node.left, curr_level+1), (curr_node.right, curr_level+1)])
        return results