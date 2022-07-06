# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head # Slow and fast start at beginning of list.
        
        while slow and fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast: # Fast caught up with slow so cycle!
                return True
            
        return False # Fast didn't catch slow before either reached None.
        
        
        
        
        