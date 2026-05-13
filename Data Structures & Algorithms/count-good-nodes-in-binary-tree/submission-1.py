# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        num_good_nodes = 0
        q = deque([(root, -math.inf)])
        while q:
            curr_node, curr_max_so_far = q.popleft()
            if not curr_node:
                continue
            if curr_node.val >= curr_max_so_far:
                num_good_nodes += 1
                curr_max_so_far = curr_node.val
            q.extend([(curr_node.left, curr_max_so_far), (curr_node.right, curr_max_so_far)])

        return num_good_nodes