"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # Solution: O(n) time, O(1) additional space.
        dummy = Node(-1)
        dummy.next = head
        
        # Stage 1: Interweave (connect orig nodes to new copy as next).
        currNode = head
        while currNode is not None:
            tempNode = Node(currNode.val)
            tempNode.next = currNode.next
            currNode.next = tempNode
            
            currNode = tempNode.next
        
        # Stage 2: Update randoms.
        currNode = head
        while currNode is not None:
            if currNode.random is not None: # currNode is an orig node.
                # currNode.next is copy of orig currNode.
                # currNode.random is orig random node, next one is new copy.
                currNode.next.random = currNode.random.next
            currNode = currNode.next.next # Go to next orig node.
            
        # Stage 3: Remove old nodes (update pointers to skip orig nodes).
        currNode = dummy
        oldNode = head
        while oldNode is not None:
            currNode.next = oldNode.next
            
            currNode = oldNode
            oldNode = currNode.next
            
        return dummy.next
        