# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def __init__(self):
    #     self.lca = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Neetcode solution
        # cur is a pointer that intends to reach the least common ancestor
        cur = root
        # while cur is not None (which will never occur since we are looking
        # for an ancestor which is not a leaf node)
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur
        # My attempt, If I didn't want to use init, I could just make a function
        # within a function
        self.lca = root
        if not root:
            return
        if root.val > p.val and root.val > q.val:
            self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            self.lowestCommonAncestor(root.right, p, q)
        return self.lca

        
"""
We need a universal value to store the LCA node.
Then, we will traverse the tree to both nodes. Every traversal will give us a 
new LCA value. The second they diverge, we will return and end the program.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # we need a pointer that searches the tree for the lca
        # we'll start at root
        pointer = root
        # while we haven't reached the end of the tree (this will never happen)
        while pointer:
            # the lca is just the node that we hit when the two nodes
            # have different comparisons to it
            # (ex. p > lca while q < lca, another ex. p == lca and q > lca)
            # this is a binary search tree: lower nodes are stored as left child
            # higher nodes are stored as right child
            # so if the node we're pointer is smaller than both of them,
            if pointer.val < p.val and pointer.val < q.val:
                # then lca is located in pointer's right subtree
                pointer = pointer.right
            # if pointer is larger than both of them
            elif pointer.val > p.val and pointer.val > q.val:
                # then lca is located in pointer's left subtree
                pointer = pointer.left
            # if we get here, we reached between both nodes (if we keep going, we'll
            # split away from at least one of the nodes)
            else:
                # we found the lca
                return pointer

