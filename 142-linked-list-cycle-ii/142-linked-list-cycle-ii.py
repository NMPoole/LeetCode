# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Tortoise and Hare solution with O(1) space and O(n) time complexity.
        if not head or not head.next: return None
        
        # Move slow and fast 1 and 2 steps ahead respectively.
        slow = head.next
        fast = head.next.next
        
        # Search for cycle using slow and fast pointers.
        while fast and fast.next:
            if fast == slow: break
            slow = slow.next
            fast = fast.next.next
            
        # No cycles.
        if slow != fast: return
        
        # If loop exists, start slow from head and fast from meeting point.
        slow = head
        
        while (slow != fast):
            slow = slow.next
            fast = fast.next
            
        return slow