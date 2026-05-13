# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = [(root, 0)]
        results = []
        while q:
            curr_node, curr_level = q.pop(0)
            
            if not curr_node:
                continue
            # print("looking at", curr_node.val)
            if len(results) < curr_level + 1:
                results.append([])
            results[curr_level].append(curr_node.val)
            q.extend([(curr_node.left, curr_level+1), (curr_node.right, curr_level+1)])
        return results