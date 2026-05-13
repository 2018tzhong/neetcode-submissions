# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        q = [(p, q)]
        while q:
            curr_node = q.pop()
            if not (
                (curr_node[0] is None and curr_node[1] is None) or
                (curr_node[0] is not None and curr_node[1] is not None and curr_node[0].val == curr_node[1].val)
            ):
                return False
            if curr_node[0]:
                q.extend([(curr_node[0].left, curr_node[1].left), (curr_node[0].right, curr_node[1].right)])
        return True
