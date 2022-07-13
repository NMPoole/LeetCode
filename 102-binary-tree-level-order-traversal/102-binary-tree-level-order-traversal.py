# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # Solution: O(n) time and O(1) additional space.
        tree = [] # Each element of 'tree' should be the node value for each level.
        
        def dfs(node, depth): # Depth-first tree traversal.
            if len(tree) <= depth:
                tree.append([])

            tree[depth].append(node.val)
            if node.left is not None:
                dfs(node.left, depth+1)
            if node.right is not None:
                dfs(node.right, depth+1)
                
        if root is not None:
            dfs(root, 0)
        
        return tree