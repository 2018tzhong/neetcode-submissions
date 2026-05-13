# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# [1, 2, 3, 5, 4] preorder
# [2, 5, 1, 3, 4] inorder

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # root = TreeNode(preorder[0])

        # iterate through preorder and create nodes
        # use map of value to node

        nodes = {}
        preorder_idxs = {}
        for i, val in enumerate(preorder):
            preorder_idxs[val] = i
            nodes[val] = TreeNode(val)

        inorder_idxs = {}
        for i, val in enumerate(inorder):
            inorder_idxs[val] = i

        root = nodes[preorder[0]]

        # then use inorder to reconstruct who is a child of whom
        # might need preorder as well

        # preorder indicates what's on a higher level
        # inorder indicates who's to the left of whom
        
        # because we're going in order, everything is to the right
        # where it gets weird is when it comes before last element in preorder
        stack = []
        # print("vals", preorder_idxs, inorder_idxs)
        for i, val in enumerate(inorder):
            # print("looking at", i, val)
            if i == 0:
                stack.append(val)
                root = nodes[stack[0]]
                last_value = val
                continue
            # if the element is after in preorder, then last_value.right is val
            if preorder_idxs[val] > preorder_idxs[last_value]:
                # print("we're getting here but idk")
                # if right already exists, we gotta just put them to left
                if nodes[last_value].right:
                    nodes[val].left = nodes[last_value].right
                nodes[last_value].right = nodes[val]                
            else:
                # else, we need to iterate through what we've seen til we see one whose preorder index is after
                # once we do, curr val is right child of that one
                p1 = len(stack) - 1
                while p1 >= 0 and preorder_idxs[val] < preorder_idxs[stack[p1]]:
                    p1 -= 1 
                if p1 == -1:
                    # then this is the root
                    # print("debug first", len(stack), p1)
                    nodes[val].left = root # old root
                    root = nodes[val]
                else:
                    # print("debug", len(stack), p1)
                    if nodes[stack[p1]].right:
                        nodes[val].left = nodes[stack[p1]].right
                    nodes[stack[p1]].right = nodes[val]
            stack.append(val) 
            last_value = val
        return root
