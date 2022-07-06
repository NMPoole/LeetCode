# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummyHead = ListNode(-1, next=head) # Dummy start for trail node and keeping head ref.
        
        # Trail is always behind the current node.
        trailNode = dummyHead
        currNode = head
        
        while currNode:
            
            if currNode.val == val: # When val matches, simply make trail skip over curr node.
                trailNode.next = currNode.next # Skipping the node.
                currNode = trailNode.next # Moving curr onto next element, trail needn't be updated.
            else: # When val not encountered, trail becomes curr node, and curr becomes next.
                trailNode = currNode
                currNode = currNode.next
            
        return dummyHead.next
        
        