# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = [root]
        while q:
            curr_node = q.pop()
            if not curr_node:
                continue
            if curr_node.val == subRoot.val:
                check = self.subTreeProcess(curr_node, subRoot)
                if check:
                    return True
            q.extend([curr_node.left, curr_node.right])
        return False

    def subTreeProcess(self, superroot, subroot):
        same = True
        q = [(superroot, subroot)]
        while q:
            left_node, right_node = q.pop()
            if not (
                (left_node is None and right_node is None) or
                (left_node is not None and right_node is not None and left_node.val == right_node.val)
            ):
                return False
            if left_node:
                q.extend([(left_node.left, right_node.left), (left_node.right, right_node.right)])
        return True