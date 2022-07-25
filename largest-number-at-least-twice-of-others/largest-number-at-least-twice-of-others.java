class Solution {
    
    public int dominantIndex(int[] nums) {
        
        // Solution: O(n) time, O(1) additional space.
        
        int maxIdx = 0;
        for (int i = 1; i < nums.length; i++) maxIdx = nums[i] > nums[maxIdx] ? i : maxIdx;
        int maxVal = nums[maxIdx];
        
        for (int num: nums) if (num != maxVal && num * 2 > maxVal) return -1;
            
        return maxIdx;
        
    }
    
}