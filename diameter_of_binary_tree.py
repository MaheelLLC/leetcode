# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Neetcode solution
        # T: O(n), I think S: O(1)
        res = [0]
        def dfs(root):
            # This line asks whether the current subtree is a null tree
            # A null tree is a tree where the root is null (0 nodes)
            if not root:
                # The height of a null tree is -1 since the height
                # of a single node is 0. A single node doesn't have 
                # a height, so a null tree must be one below that (-1)
                # This allows for the math of heights and diameters to work out
                return -1
            # Okay, so dfs actually returns the height of the node placed in its
            # parameter. We recursively go down until we hit the child nodes of
            # the leaf nodes which are null trees/nodes.
            # Once we reach the base case of null trees, we return -1 and go to
            # their parents (the leaf nodes). Once we recursively go back to the 
            # leaf nodes, we use the -1 and store it on left and right. Left and 
            # right will now always store the heights of parameter node's left 
            # and right subtrees. We use these two values to calculate the 
            # parameter node's max diameter (which is stored in res[0]) and 
            # the parameter node's height (which is the return value of dfs
            # aka 1 + max(left, right))
            left = dfs(root.left)
            right = dfs(root.right)
            res[0] = max(res[0], 2 + left + right)
            return 1 + max(left, right)
        dfs(root)
        return res[0]

        # My attempt
        self.dfs(root.left, 1)
        left = self.max_depth
        self.max_depth = 0
        self.dfs(root.right, 1)
        right = self.max_depth
        return left + right


    # Part of my attempt
    def __init__(self):
        self.max_depth = 0

    # Also part of my attempt
    def dfs(self, node, depth):
        if node is None:
            return
        self.max_depth = max(self.max_depth, depth)
        self.dfs(node.left, depth + 1)
        self.dfs(node.right, depth + 1)



"""
We conduct a DFS on both the left and right subtrees of root
We add them and that's our result. False, the root will not 
always contain the max diameter.
"""