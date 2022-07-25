class Solution {
    
    public int pivotIndex(int[] nums) {
        
        // Solution: O(n) time, and O(1) additional space.
        int sum = 0, leftSum = 0;
        
        for (int x: nums) sum += x; // Calcuating sum of all elements.
        
        for (int i = 0; i < nums.length; ++i) {
            
            if (leftSum == sum - leftSum - nums[i]) return i; // Check if left- and right-ward sums are the same.
            leftSum += nums[i]; // Otherwise, simply increase the left-ward sum.
            
        }
        
        return -1;
        
    }
    
}