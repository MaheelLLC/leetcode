# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Optimal code that I found which is cool
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

        # Neetcode solution
        if not root:
            return None
        # Swap the children
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

        # My attempt
        if root:
            if root.left and root.right:
                self.invertTree(root.left)
                self.invertTree(root.right)
                # temp = TreeNode(root.left.val, root.left.left, root.left.right)
                temp = root.left
                root.left = root.right
                root.right = temp
            elif root.left:
                self.invertTree(root.left)
                root.right = root.left
                root.left = None
            elif root.right:
                self.invertTree(root.right)
                root.left = root.right
                root.right = None
        return root


"""
Problem is asking me to flip the left and right child for every node in a tree.
It sounds like a recursive solution where we start with the leaf nodes and then
work our way up (bottom up) approach. We use the base case to be the leaf nodes.
Then, we go up a level and start flipping children (we might need a temp 
TreeNode for flipping). To reach the leaves immediately, we'll use depth first 
search (postorder search too). False, bottom up is not required. It can be top
down too.

Change of plans: I used four different cases.
1. root has two children
2. root has left child only
3. root has right child only
4. root has no children
Case 1:
recursively call function on both children
Once done, swap them (post order)
Case 2 and 3:
recursively call function on child
Once done, swap child with None
Case 4:
just return the leaf node
"""
