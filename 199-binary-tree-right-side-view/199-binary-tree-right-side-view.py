# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        rightNodes = defaultdict(int) # Dictionary to store visible node from right-side at each depth.
        
        # Recursively fill rightNodes with DFS by looking right first, then considering left if no right node.
        def dfs(node, depth):
            if node is None:
                return
            if depth not in rightNodes:
                rightNodes[depth] = node.val

            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        
        dfs(root, 0)
        
        # Simply return values of the dictionary, which are nodes visible from the right-side.
        return rightNodes.values()
        
        
        
            
        
    