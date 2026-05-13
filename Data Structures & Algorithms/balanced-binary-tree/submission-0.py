# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        balanced = True
        def height_recurse(node):
            nonlocal balanced
            if not node:
                return 0
            left_height = height_recurse(node.left)
            right_height = height_recurse(node.right)
            if abs(left_height - right_height) > 1:
                # print("not balanced", node.val, left_height, right_height)
                balanced = False
            return 1 + max(left_height, right_height)

        result = height_recurse(root)
        return balanced
