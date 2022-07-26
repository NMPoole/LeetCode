# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Solution: O(N) time - N is num of nodes in the tree - and O(H) additional space - H is height of the tree.
        
        if root == None or root == p or root == q: # LCA if p or q is root has to be root.
            return root
        
        left = right = None # Look in left and right child.
        if root.left:
            left = self.lowestCommonAncestor(root.left, p, q)
        if root.right:
            right = self.lowestCommonAncestor(root.right, p, q)

        if left and right: # If both children returned a node, means both p and q found so parent is LCA.
            return root
        else: # Either one of the chidren returned a node, meaning either p or q found on left or right branch.
            return left or right