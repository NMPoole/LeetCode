/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        
        // Solution: O(n) time, O(1) space complexity.
        ListNode currA = headA, currB = headB;
        
        // Find the lengths of each of the linked lists.
        int lenA = 0, lenB = 0;
        while (currA != null) {
            lenA += 1;
            currA = currA.next;
        }
            
        while (currB != null) {
            lenB += 1;
            currB = currB.next;
        }
            
        // Determine longer and shorter of each list and diff in lengths.
        ListNode currLong;
        int diff;
        ListNode currShort;
        
        if (lenA > lenB) {
            currLong = headA;
            diff = lenA - lenB;
            currShort = headB;
        } else {
            currLong = headB;
            diff = lenB - lenA;
            currShort = headA;
        }
            
        // Move forward diff places in the longer linked list.
        int i = 0;
        while (i < diff) {
            i += 1;
            currLong = currLong.next;
        }
            
        // Find location where the linked lists intersect, if exists.
        while (currLong != currShort) {
            currLong = currLong.next;
            currShort = currShort.next;
        }
            
        // They both would have met at the same time.
        // Either they both met and are None, which means no intersection.
        // Or, they both met before list end and are at the same node.
        return currLong;
        
    }
    
}