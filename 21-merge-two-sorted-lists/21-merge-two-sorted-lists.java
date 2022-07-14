/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        
        // Solution: O(n) time, O(1) space.
        
        ListNode dummy = new ListNode(-1); // Keep reference to list head.
        ListNode output = dummy;
            
        ListNode currL1 = list1;
        ListNode currL2 = list2;
        
        // Iterate over all elements from both lists and merge into output.
        while (currL1 != null && currL2 != null) {
            
            if (currL1.val < currL2.val) {
                output.next = currL1;
                currL1 = currL1.next;
            } else {
                output.next = currL2;
                currL2 = currL2.next;
            }
              
            output = output.next;
                    
        }
            
        // There may be lingering nodes in a longer list to add.
        if (currL1 != null) {
            output.next = currL1;
        }
        if (currL2 != null) {
            output.next = currL2;
        }
            
        return dummy.next;
        
    }
    
}