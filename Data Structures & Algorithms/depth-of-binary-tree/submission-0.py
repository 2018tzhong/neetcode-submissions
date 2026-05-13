# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = [(root, 0)]
        max_depth = 0
        while q:
            curr_node = q.pop()
            if not curr_node[0]:
                max_depth = max(max_depth, curr_node[1])
                continue
            q.extend([(curr_node[0].left, curr_node[1]+1), (curr_node[0].right, curr_node[1]+1)])
        return max_depth