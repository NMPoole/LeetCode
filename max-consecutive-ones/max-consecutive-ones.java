class Solution {
    
    public int findMaxConsecutiveOnes(int[] nums) {
        
        // Solution: O(n) time, O(1) additional space.
        
        int count = 0;
        int maxCount = 0;
        
        for (int num: nums) {
            
            if (num == 1) {
                count += 1;
                maxCount = Math.max(maxCount, count);
            } else {
                count = 0;
            }
            
        }
        
        return maxCount;

    }
    
}