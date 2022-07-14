class Solution {
    
    public boolean isPalindrome(String s) {
        
        // Solution: O(n) time, O(1) additional space.
        
        int l = 0;
        int r = s.length() - 1;
        
        while (l < r) {
            
            char sl = s.charAt(l);
            char sr = s.charAt(r);
            
            // Skip over non-alphanumeric chars.
            while (l < r && !Character.isLetterOrDigit(sl)) {
                l += 1;
                sl = s.charAt(l);
            }
                
            while (r > l && !Character.isLetterOrDigit(sr)) {
                r -= 1;
                sr = s.charAt(r);
            }
            
            // Check chars are the same on both sides.
            if (Character.toLowerCase(sl) != Character.toLowerCase(sr)) {
                return false;  
            }
            
            l += 1;
            r -= 1;
                    
        }
            
        return true;
        
    }  
    
}