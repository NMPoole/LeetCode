# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # This solution runs in O(n) time with O(1) space complexity.
        currA, currB = headA, headB
        
        # Find the lengths of each of the linked lists.
        lenA, lenB = 0, 0
        while currA:
            lenA += 1
            currA = currA.next
        while currB:
            lenB += 1
            currB = currB.next
        
        # Determine longer and shorter of each list and diff in lengths.
        if lenA > lenB:
            currLong = headA
            diff = lenA - lenB
            currShort = headB
        else:
            currLong = headB
            diff = lenB - lenA
            currShort = headA
            
        # Move forward diff places in the longer linked list.
        i = 0
        while i < diff:
            i += 1
            currLong = currLong.next
            
        # Find location where the linked lists intersect, if exists.
        while currLong != currShort:
            currLong = currLong.next
            currShort = currShort.next
            
        # They both would have met at the same time.
        # Either they both met and are None, which means no intersection.
        # Or, they both met before list end and are at the same node.
        return currLong
            
        