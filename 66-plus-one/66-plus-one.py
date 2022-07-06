class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        index = 0 # End of the array
        mustIncrement = True
        
        while mustIncrement: # Handle digit increments for all indices.
            index -= 1
            
            if index < -len(digits): # Must add a column and shift the array.
                digits.insert(0, 1) # Add the new most significsant digit.
                mustIncrement = False
            else: # Simply increment index digit and move on.
                digits[index] = (digits[index] + 1) % 10
                mustIncrement = digits[index] == 0
            
        return digits