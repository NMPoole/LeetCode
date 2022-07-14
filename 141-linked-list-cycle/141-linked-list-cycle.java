/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    
    public boolean hasCycle(ListNode head) {
        
        ListNode slow = head, fast = head; // Slow and fast start at beginning of list.
        
        while (slow != null && fast != null && fast.next != null) {
            
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) return true; // Fast caught up with slow so cycle!   
                
        }
            
        return false; // Fast didn't catch slow before either reached None.
        
    }
    
}