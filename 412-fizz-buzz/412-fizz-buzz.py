class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # Solution: O(n) time requiring O(n) space for the output array.
        strings = []
        
        for i in range(1, n + 1): # 1-indexed array desired.
            
            divBy3 = i % 3 == 0
            divBy5 = i % 5 == 0
            
            if divBy3 and divBy5:
                strings.append("FizzBuzz")
            elif divBy3:
                strings.append("Fizz")
            elif divBy5:
                strings.append("Buzz")
            else:
                strings.append(str(i))
                
        return strings