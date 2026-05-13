# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # get paths to two nodes, save those paths
        queue = [(root, [])]
        p_path = []
        q_path = []
        while queue:
            curr_node, curr_path = queue.pop()
            if not curr_node:
                continue
            # print("looking at", curr_node.val)
            # print("check", curr_node.val == p.val, curr_node == p, curr_node.val == q.val, curr_node == q)
            if curr_node.val == p.val:
                p_path = curr_path
            if curr_node.val == q.val:
                q_path = curr_path
            curr_path.append(curr_node)
            queue.extend([(curr_node.left, list(curr_path)), (curr_node.right, list(curr_path))])
            # print("new q", q)
        
        lca = None
        p_path_values = [i.val for i in p_path]
        q_path_values = [i.val for i in q_path]
        # print(p_path_values, q_path_values)
        for i in p_path:
            if i.val in q_path_values:
                lca = i
        return lca