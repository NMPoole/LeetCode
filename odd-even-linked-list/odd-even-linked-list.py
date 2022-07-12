# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Solution: O(n) time, O(1) additional space.
        #           , where n is the number of nodes in the linked list.
        
        even_temp = even = ListNode(-1) # Dummy for even node list.
        odd_temp = odd = ListNode(-2) # Dummy for odd node list.
        
        count = 1
        currNode = head
        
        # Iterate over all nodes in the linked list.
        while currNode is not None:
            
            # Adding even and odd indexed nodes to corresponding list.
            if count % 2 == 0:
                even.next = currNode
                even = even.next
            else:
                odd.next = currNode
                odd = odd.next
                
            currNode = currNode.next
            count += 1
        
        odd.next = even_temp.next # Attach even list to tail of odd list.
        even.next = None # Last node must point to None to signify end.
        
        return odd_temp.next # Return head of the new list.