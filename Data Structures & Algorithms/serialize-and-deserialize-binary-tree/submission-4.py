# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        results = ""
        q = deque([root])
        while q:
            curr_node = q.popleft()
            # print("looking at ", curr_node)
            if not curr_node:
                results = results + ".,"
                continue
            results = results+ str(curr_node.val)+ ","
            q.extend([curr_node.left, curr_node.right])
            # print("curr results", results)
        print("final results", results)
        return results
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if len(data) == 0:
            return None
        els = deque(data.split(","))
        left = 1
        root = TreeNode(els[0])
        q = deque([root])
        while q:
            curr_node = q.popleft()
            # todo add check for left to avoid out of bounds
            if left < len(els) - 1:
                temp_val1 = els[left]
                if temp_val1 != "." and temp_val1 != "":
                    curr_node.left = TreeNode(temp_val1)
                    q.append(curr_node.left)
                left += 1

            if left < len(els) - 1:
                temp_val2 = els[left]
                if temp_val2 != "." and temp_val2 != "":
                    curr_node.right = TreeNode(temp_val2)
                    q.append(curr_node.right)
                left += 1
            # left += 2
        return root

