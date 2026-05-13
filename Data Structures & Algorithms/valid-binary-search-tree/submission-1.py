# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        results = []
        # q = [root]
        # while q:
        #     curr_node = q.pop()
        #     if not curr_node:
        #         continue
        #     results.append(curr_node.val)
        #     q.extend([curr_node.right, curr_node.left])


        def dfs(node):
            nonlocal results
            if not node:
                return
            dfs(node.left)
            results.append(node.val)
            dfs(node.right)

        dfs(root)
        # print(results)
        for i in range(1, len(results)):
            if results[i] <= results[i-1]:
                return False
        
        return True

