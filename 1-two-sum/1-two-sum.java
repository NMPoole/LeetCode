class Solution {
    
    public int[] twoSum(int[] nums, int target) {
        
        // Solution: O(n) time complexity, and O(n) space complexity.
        
        // Dictionary of values in nums to their corresponding index.
        HashMap<Integer, Integer> values = new HashMap<Integer, Integer>();
        
        for (int i = 0; i < nums.length; i++) {
            int val = nums[i];
                
            // If the number required in dictionary, we have the answer.
            if (values.containsKey(target - val)) { 
                return new int[]{values.get(target - val), i};
            } else { // Otherwise, make an entry for the current value.
                values.put(val, i);
            }
            
        }
        
        return new int[2];
                    
    }
    
}