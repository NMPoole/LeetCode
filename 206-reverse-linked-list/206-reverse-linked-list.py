# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # This solution runs in O(n) time and O(1) space.
        
        if not head or not head.next: # Empty or singleton list trivially reversed.
            return head
        
        currNode = head.next
        head.next = None # Becomes the end of the list, so next is None.
        
        while currNode: # For every subsequent list item, set as head.
            temp = currNode.next
            currNode.next = head
            head = currNode
            currNode = temp
            
        return head