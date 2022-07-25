class Solution {
    
    public String longestCommonPrefix(String[] strs) {
        
        // Solution: O(n) time, O(1) additional space.
        // Longest common prefix will be the intersection between the minimum and maximum string.
        
        if (strs.length == 0) return "";
        
        String maxStr = Arrays.asList(strs)
            .stream().max(Comparator.comparing(String::toLowerCase)).get();
        String minStr = Arrays.asList(strs)
            .stream().min(Comparator.comparing(String::toLowerCase)).get();
        int match = 0;
        
        while (match < maxStr.length() && 
               match < minStr.length() && 
               maxStr.charAt(match) == minStr.charAt(match)) match += 1;
            
        return maxStr.substring(0, match);
        
    }
    
}