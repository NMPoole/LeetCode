# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Solution: O(n) time, O(1) space.
        
        # Get length of the linked list.
        currNode = head
        n = 0
        while currNode is not None:
            n += 1
            currNode = currNode.next
        
        # Get pointers to the start and middle nodes of the linked list.
        mid = n // 2
        i = 0
        first = second = head
        while i < mid: 
            second = second.next
            i += 1
            
        second = self.reverse(second) # Reverse the 2nd half of list.
        
        # Iterate nodes in 1st and reverse 2nd halves. Check values same.
        while first is not None and second is not None:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
            
        return True
        
        
    def reverse(self, head):
        ans = None

        while head is not None:
            nextNode = head.next
            head.next = ans
            ans = head
            head = nextNode

        return ans
        
        
                
                