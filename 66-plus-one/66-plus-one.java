class Solution {
    
    public int[] plusOne(int[] digits) {
        
        // Solution: O(n) time, O(1) additional space.
        
        int n = digits.length;
        
        for (int i = n - 1; i >= 0; i--) {
            
            if (digits[i] < 9) {
                digits[i] += 1;
                return digits;
            }
            
            digits[i] = 0; // When digit is 9, have to set digit to 0 and carry.
            
        }
        
        // Handle most significant digit carries that need the array to be extended.
        digits = new int[n + 1];
        digits[0] = 1;
            
        return digits;
        
    }
    
}