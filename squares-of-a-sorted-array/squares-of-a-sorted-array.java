class Solution {
    
    public int[] sortedSquares(int[] nums) {
        
        // First, square all numbers in nums for O(n) time.
        for (int i = 0; i < nums.length; i++) {
            nums[i] = nums[i] * nums[i];
        }
            
        // Then, sort the nums array in presumably O(n logn) time.
        Arrays.sort(nums);
        return nums;
        
    }
    
}