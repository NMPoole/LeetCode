class Solution {
    
    public int singleNumber(int[] nums) {
        
        int result = nums[0];
        
        // XOR of duplicate numbers zero-out, so result after XORing all nums is the one with no duplicate.
        for (int i = 1; i < nums.length; i++) result ^= nums[i]; 
         
        return result;
        
    }
    
}