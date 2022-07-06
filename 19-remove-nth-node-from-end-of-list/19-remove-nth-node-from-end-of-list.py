# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # This solution is O(n) time (one pass only), with O(1) space.
        
        # Create dummy to handle edge cases and keep a head ref.
        dummy = slow = fast = ListNode(-1, next=head)
        
        # Move fast pointer ahead by n steps.
        for _ in range(n):
            fast = fast.next
            
        # Move both pointers until fast.next is None.
        # Slow will be the element before the one to delete.
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        # Delete node.
        slow.next = slow.next.next
        
        return dummy.next