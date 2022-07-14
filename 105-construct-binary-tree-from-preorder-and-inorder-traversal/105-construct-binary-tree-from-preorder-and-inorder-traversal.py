# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # Solution: O(n) time, O(n) additional space.
        
        self.preOrderIndex = 0
        
        # Build a hashmap to store value -> index in inorder relations.
        self.inOrderIndexMap = {}
        for index, value in enumerate(inorder):
            self.inOrderIndexMap[value] = index
        
        def arrayToTree(left, right):
            if left > right: return None # No elements to construct the tree.
            
            # Select the preOrderIndex element as the root and increment it.
            rootValue = preorder[self.preOrderIndex]
            root = TreeNode(rootValue)

            self.preOrderIndex += 1

            # Build left and right subtree, excluding inOrderIndexMap[rootValue] element because it's the root.
            root.left = arrayToTree(left, self.inOrderIndexMap[rootValue] - 1)
            root.right = arrayToTree(self.inOrderIndexMap[rootValue] + 1, right)

            return root
        
        return arrayToTree(0, len(preorder) - 1)