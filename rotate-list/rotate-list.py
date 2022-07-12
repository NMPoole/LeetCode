# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None: return head
        
        # Get length of the linked list.
        length, tail = 1, head
        while tail.next is not None:
            tail = tail.next
            length += 1
            
        k = k % length # Don't need to perform full list cycles.
        if k == 0: return head # Don't do anything if just a full cycle.
        
        # Move to the right and rotate.
        # Don't actually need to move nodes, just alter pointers.
        currNode = head
        for i in range(length - k - 1):
            currNode = currNode.next
            
        newHead = currNode.next
        currNode.next = None
        tail.next = head # Connect end to beginning for cyclic list.
        
        return newHead