# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = [root]
        while q:
            curr_node = q.pop()
            if not curr_node:
                continue
            curr_node.left, curr_node.right = curr_node.right, curr_node.left
            q.extend([curr_node.left, curr_node.right])
            # q.append(curr_node.right)
        return root