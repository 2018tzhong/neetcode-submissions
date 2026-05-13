# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_path_sum = -math.inf
        def recurse(node):
            nonlocal max_path_sum
            if not node:
                return 0
            left_sum = max(recurse(node.left), 0)
            right_sum = max(recurse(node.right), 0)
            max_path_sum = max(max_path_sum, left_sum + right_sum + node.val)
            return max(left_sum, right_sum) + node.val
        
        # left_path = recurse(root.left)
        # right_path = recurse(root.right)
        # max_reg_path = max(max(left_path, 0)+)
        # return max(max_path_sum, left_path + root.val + right_path, root.val)
        recurse(root)
        return max_path_sum