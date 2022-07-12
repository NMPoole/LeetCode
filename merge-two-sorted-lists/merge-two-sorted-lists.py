# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = output = ListNode(val=-1) # Keep reference to list head.
        currL1 = list1
        currL2 = list2
        
        # Iterate over all elements from both lists and merge into output.
        while currL1 is not None and currL2 is not None:
            
            if currL1.val < currL2.val:
                output.next = currL1
                currL1 = currL1.next
            else:
                output.next = currL2
                currL2 = currL2.next
                
            output = output.next
        
        # There may be lingering nodes in a longer list to add.
        if currL1 is not None:
            output.next = currL1
        if currL2 is not None:
            output.next = currL2
            
        return dummy.next