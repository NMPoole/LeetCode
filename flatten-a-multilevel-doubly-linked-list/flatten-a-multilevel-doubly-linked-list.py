"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # Solution: O(n) time as visit every node once. O(1) additional space as updating pointers.
        self.flattenChildren(head)
        return head
    
    
    def flattenChildren(self, head=None):

        prevNode, currNode = None, head

        while currNode is not None:

            if currNode.child is not None:

                currChild = currNode.child
                currTail = self.flattenChildren(currChild) # Flatten child list, get end of flatten.
                
                # After next level flattening is completed...
                # ...handle the concatenation between current linked list and child linked list.

                currNode.child = None # currNode's child points to None after flattening.
                
                # Update pointers between orig. next and curr tail. 
                origNext = currNode.next 
                if origNext is not None: origNext.prev = currTail
                currTail.next = origNext

                # Update pointers between currNode and currChild
                currNode.next, currChild.prev = currChild, currNode

                # Update prev and cur by moving to next position.
                prevNode, currNode = currTail, origNext

            else:

                # Update prev and cur by moving to next position
                prevNode, currNode = currNode, currNode.next

        return prevNode # Return tail node.
    