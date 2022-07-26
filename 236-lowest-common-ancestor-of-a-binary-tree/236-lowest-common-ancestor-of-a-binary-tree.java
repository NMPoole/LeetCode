/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        
        // Solution: O(N) time - N is num of nodes in the tree - and O(H) additional space - H is height of the tree.
        
        if (root == null || root == p || root == q) return root; // LCA if p or q is root has to be root.
        
        TreeNode left = null, right = null; // Look in left and right child.
        if (root.left != null) left = this.lowestCommonAncestor(root.left, p, q);
        if (root.right != null) right = this.lowestCommonAncestor(root.right, p, q);

        // If both children returned a node, means both p and q found so parent is LCA.
        // Else, either one of the chidren returned a node, meaning either p or q found on left or right branch.
        if (left != null && right != null) return root;
        else return (left != null) ? left : right;
        
    }
    
}