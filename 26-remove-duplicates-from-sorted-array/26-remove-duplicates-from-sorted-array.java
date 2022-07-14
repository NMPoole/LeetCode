class Solution {
    
    public int removeDuplicates(int[] nums) {
        
        // Solution: O(n) time, O(1) additional space.
        
        if (nums.length < 2) {
            return nums.length;
        }
            
        int i = 0;  // Slow-run pointer.
        
        for (int j = 0; j < nums.length; j++) {
            
            int value = nums[j];
                
            if (value == nums[i]) {
                continue;
            }
            
            // Else, capture the result
            i += 1;
            
            if (i != j) {
                nums[i] = value; // In place overriden.
            }
            
        }
        
        return i + 1;
        
    }
    
}