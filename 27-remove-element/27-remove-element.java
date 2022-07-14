class Solution {
    
    public int removeElement(int[] nums, int val) {
        
        // Solution: O(n) time, with O(1) space.
        //   Iterate all nums, only copying values that are not val.
        //   i does not increase when val found, so val is overwritten by subsequent numbers.
        //   i is last index overwritten, and therefore the new length to be considered.
        
        int i = 0;
        
        for (int x : nums) {
            
            if (x != val) {
                nums[i] = x;
                i += 1;
            }
            
        }
                
        return i;
        
    }
    
}