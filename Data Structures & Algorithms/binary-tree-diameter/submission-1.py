# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        max_path = 0
        def dfs_recurse(node):
            nonlocal max_path
            if not node:
                return 1
            left_path = dfs_recurse(node.left)
            right_path = dfs_recurse(node.right)
            # print("checking", node.val, left_path, right_path)
            max_path = max(max_path, left_path - 1 + right_path - 1)
            # print("max_path", max_path)
            return max(1 + left_path, 1 + right_path)
        left_root = dfs_recurse(root.left)
        right_root = dfs_recurse(root.right)
        # print("last check", max_path)
        return max(max_path, left_root - 1 + right_root - 1)