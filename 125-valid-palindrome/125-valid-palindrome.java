class Solution {
    
    public boolean isPalindrome(String s) {
        
        // Solution: O(n) time, O(1) additional space.
        
        s = s.toLowerCase();
        int l = 0;
        int r = s.length() - 1;
        
        while (l < r) {
            
            // Skip over non-alphanumeric chars.
            while (l < r && !Character.isLetterOrDigit(s.charAt(l))) l += 1;
            while (r > l && !Character.isLetterOrDigit(s.charAt(r))) r -= 1;
            
            // Check chars are the same on both sides.
            if (s.charAt(l) != s.charAt(r)) return false;  
            
            l += 1;
            r -= 1;
                    
        }
            
        return true;
        
    }  
    
}