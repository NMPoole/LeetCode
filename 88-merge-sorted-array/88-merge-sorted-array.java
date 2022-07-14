class Solution {
    
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        
        // Solution: O(n) time, with O(1) additional space.
        
        while (n > 0) { // While still numbers to intertwine in nums2, iterate backwards across both lists.
            
            // If no nums left to intertwine from nums1, or curr num2 >= curr num1, use curr num2.
            // Otherwise, use curr num1. In both cases, update index of array value used from.
            if (m <= 0 || nums2[n-1] >= nums1[m-1]) {
                nums1[m+n-1] = nums2[n-1];
                n -= 1;
            } else {
                nums1[m+n-1] = nums1[m-1];
                m -= 1;
            }
        
        }
        
    }
    
}