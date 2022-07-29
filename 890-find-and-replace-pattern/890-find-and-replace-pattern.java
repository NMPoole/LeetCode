class Solution {
    
    public List<String> findAndReplacePattern(String[] words, String pattern) {
        
        // Solution: O(n m) time - n is num words and m is length of words - O(n) additional space.
        // Note: Java translation of my Python solution.
        
        List<String> output = new ArrayList<String>();
        
        for (String word: words) if (this.check(word, pattern)) output.add(word);
        
        return output;
            
    }
    
    public boolean check(String word, String pattern) {
        
        HashMap<Character, Character> m1 = new HashMap<>();
        HashMap<Character, Character> m2 = new HashMap<>();
        
        for (int i = 0; i < word.length(); i++) {
            
            char a = word.charAt(i);
            char b = pattern.charAt(i);
            
            if (!m1.containsKey(a)) m1.put(a, b);
            if (!m2.containsKey(b)) m2.put(b, a);
                
            if (a != m2.get(b) || b != m1.get(a)) return false;
            
        }
        
        return true;
        
    }

    
}